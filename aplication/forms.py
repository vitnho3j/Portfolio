from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile, Occupation, ProfileSocialMedia, SocialMedia
from ckeditor.widgets import CKEditorWidget
import re
from django.core.validators import URLValidator, RegexValidator


class UpdateRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UpdateRegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'update-form'
        self.fields['username'].widget.attrs['placeholder'] = 'Nome de usuário'
        self.fields['username'].label = 'Username'
        self.fields['username'].help_text = '<span class="spn-form-update"><small>O nome de usuário pode ter até 150 caracteres, letras, digitos, e @/./+/-/_ apenas.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'update-form'
        self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
        self.fields['password1'].label = 'Senha'
        self.fields['password1'].help_text = '<ul class="spn-form-update small"><li>Sua senha não pode ser muito parecida com suas outras informações pessoais.</li><li>Sua senha deve conter pelo menos 8 caracteres.</li><li>Sua senha não pode ser uma senha comumente usada.</li><li>Sua senha não pode ser inteiramente numérica.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'update-form'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirme a senha'
        self.fields['password2'].label = 'Confirmação da senha'
        self.fields['password2'].help_text = '<span class="spn-form-update"><small>Digite a mesma senha de antes, para verificação.</small></span>'

    def clean_username(self):
        form_username = self.cleaned_data.get('username')
        current_user = self.instance
        if current_user.username == form_username:
            return current_user.username
        if User.objects.filter(username=form_username).exists():
            raise forms.ValidationError("Este nome de usuário já está em uso. Por favor, escolha outro.")
        return form_username
        
class UpdatePersonalForm(UserChangeForm):
    first_name = forms.CharField(label='Primeiro nome', max_length=100, widget=forms.TextInput(attrs={'class':'update-form', 'placeholder':'Primeiro nome'}))
    last_name = forms.CharField(label='Segundo nome', max_length=100, widget=forms.TextInput(attrs={'class':'update-form', 'placeholder':'Último nome'}))
    password = None

    class Meta:
        model = User
        fields = ('first_name','last_name')
    
    def __init__(self, *args, **kwargs):
        super(UpdatePersonalForm, self).__init__(*args, **kwargs)


class CustomCKEditorWidget(CKEditorWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config['removeButtons'] = ['Source', 'Table', 'Link', 'Anchor', 'Smiley', 'SpecialChar', 'Unlink', 'Resize', 'TextColor']
        self.config['removePlugins'] = 'image'

class ProfileUpdateForm(forms.ModelForm):
    def validate_description_length(value):
        max_length = 1000
        if len(value) > max_length:
            raise forms.ValidationError(f'A descrição não pode exceder {max_length} caracteres (você digitou {len(value)} caracteres.)')
    
    photo = forms.ImageField(label='Foto de perfil')
    description = forms.CharField(label='Sua descrição', max_length=1000, widget=CustomCKEditorWidget(), validators=[validate_description_length], error_messages={'max_length': ''})
    occupation = forms.ModelChoiceField(label='Sua ocupação', queryset=Occupation.objects.all(), empty_label=None, widget=forms.Select(attrs={'class':'update-form'}))

    class Meta:
        model = Profile
        fields = ('photo', 'description', 'occupation')
    
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)

    def clean_photo(self):
        photo = self.cleaned_data.get('photo', False)
        if photo:
            limit = 2*1024*1024
            if photo.size > limit:
                raise forms.ValidationError("O arquivo de imagem é muito largo ( Limite máximo: 2mb )")
            return photo
        else:
            raise forms.ValidationError("A imagem carregada não pode ser lida")


class AddSocialMediaForm(forms.ModelForm):
    social_media = forms.ModelChoiceField(label='Escolha uma rede social', empty_label=None, queryset=SocialMedia.objects.all(), widget=forms.Select(attrs={'class':'update-form'}))
    identification = forms.CharField(required=True, label='Identificação da rede social', widget=forms.TextInput(attrs={'class':'update-form'}), help_text='Insira o número para adicionar o whatsapp no formato cód país + ddd + número, ex: (+55)24981094563 ou link do perfil para todas as outras redes.')

    class Meta:
        model = ProfileSocialMedia
        fields = ('social_media', 'identification')
    
    def __init__(self, *args, profile=None, **kwargs):
        if profile is not None:
            self.profile = profile
        else:
            raise forms.ValidationError("Incapaz de reconhecer o usuário atual.")
        super(AddSocialMediaForm, self).__init__(*args, **kwargs)

    def clean_identification(self):
        identification = self.cleaned_data.get('identification', False)
        social_media = self.cleaned_data.get('social_media', False)
        if social_media.is_link == False:
            number_validator = RegexValidator(regex='^\(\d{2}\)\d{11}$', message='A identificação deve estar no formato (+55)24981094563.')
            if len(identification) > 16:
                raise forms.ValidationError("O número de telefone não pode exceder 16 caracteres, por favor, revise o número para garantir que não tenha digitado incorretamente.")
            
            if len(identification) < 16:
                raise forms.ValidationError("O número de telefone não pode ser menor do que 16 caracteres, por favor, revise o número para garantir que não tenha digitado incorretamente.")
            
            number_validator(identification)
        else:
            validate = URLValidator
            try:
                validate(identification)
            except:
                raise forms.ValidationError("A identificação fornecida não é um URL válido")
                
        return identification

    def clean_social_media(self):
        limit = 6
        socials = self.profile.medias.all()
        if socials.count() >= limit:
            raise forms.ValidationError("Você atingiu o limite(6) de redes socias que podem ser adicionadas, altere ou exclua uma rede social existente.")
        return self.cleaned_data.get('social_media', False)