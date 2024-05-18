from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile, Occupation, ProfileSocialMedia, SocialMedia, Comment
from ckeditor.widgets import CKEditorWidget


class UpdateRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','password1', 'password2')
        error_messages = {
            'password_mismatch': "As senhas não correspondem. Por favor, tente novamente."
        }

    def __init__(self, *args, **kwargs):
        super(UpdateRegisterForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'container-input'
        self.fields['username'].widget.attrs['placeholder'] = 'Nome de usuário'
        self.fields['username'].label = 'Username'
        self.fields['username'].help_text = '<span class="spn-form"><small>O nome de usuário pode ter até 150 caracteres, letras, digitos, e @/./+/-/_ apenas.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'container-input'
        self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
        self.fields['password1'].label = 'Senha'
        self.fields['password1'].help_text = '<div><ul class="spn-form" id="ul"><small><li>Sua senha não pode ser muito parecida com suas outras informações pessoais.</li><li>Sua senha deve conter pelo menos 8 caracteres.</li><li>Sua senha não pode ser uma senha comumente usada.</li><li>Sua senha não pode ser inteiramente numérica.</li></small></ul></div>'

        self.fields['password2'].widget.attrs['class'] = 'container-input'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirme a senha'
        self.fields['password2'].label = 'Confirmação da senha'
        self.fields['password2'].help_text = '<span class="spn-form"><small>Digite a mesma senha de antes, para verificação.</small></span>'


    def clean_username(self):
        form_username = self.cleaned_data.get('username')
        current_user = self.instance
        if current_user.username == form_username:
            return current_user.username
        if User.objects.filter(username=form_username).exists():
            raise forms.ValidationError("Este nome de usuário já está em uso. Por favor, escolha outro.")
        return form_username
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("As senhas não correspondem. Por favor, tente novamente.")
        return password2
        

class UpdatePersonalForm(UserChangeForm):
    first_name = forms.CharField(label='Primeiro nome', max_length=100, widget=forms.TextInput(attrs={'class':'container-input', 'placeholder':'Primeiro nome'}))
    last_name = forms.CharField(label='Segundo nome', max_length=100, widget=forms.TextInput(attrs={'class':'container-input', 'placeholder':'Último nome'}))
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
    description = forms.CharField(label='Descrição', max_length=1000, widget=CustomCKEditorWidget(attrs={'class': 'ck-editor', 'id': 'descricao-field'}), validators=[validate_description_length], error_messages={'max_length': ''})
    occupation = forms.ModelChoiceField(label='Ocupação', queryset=Occupation.objects.all(), empty_label=None, widget=forms.Select(attrs={'class':'update-form'}))

    class Meta:
        model = Profile
        fields = ('photo', 'description', 'occupation')
    
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required':'O campo {fieldname} é obrigatório'.format(
                fieldname=field.label)}

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
    social_media = forms.ModelChoiceField(label='Escolha uma rede social', empty_label=None, queryset=SocialMedia.objects.all(), widget=forms.Select(attrs={'class':'container-input'}))
    identification = forms.CharField(required=True, label='Identificação da rede social', widget=forms.TextInput(attrs={'class':'container-input'}), help_text='Insira o número para adicionar o whatsapp no formato cód país + ddd + número, ex: 5524981094563, o seu endereço de email para o email, ou link do perfil para todas as outras redes.')

    class Meta:
        model = ProfileSocialMedia
        exclude = ('profile',)
        
    def __init__(self, *args, **kwargs):
        self.profile = kwargs.pop('profile', None)
        super(AddSocialMediaForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        instance = super().save(commit=False)
        instance.profile = self.profile
        return cleaned_data
    
class AddTestimonialsForm(forms.ModelForm):
    comment = forms.CharField(required=True, label='Escreva seu testemunho', widget=forms.Textarea(attrs={'class':'container-input', 'id': 'text-area'}), help_text="Insira seu relato sobre Vitor Daniel, o seu texto não pode ultrapassar 1500 caracteres")

    class Meta:
       model = Comment 
       exclude = ('profile',)

    def __init__(self, *args, **kwargs):
        self.profile = kwargs.pop('profile', None)
        super(AddTestimonialsForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        instance = super().save(commit=False)
        instance.profile= self.profile
        return cleaned_data