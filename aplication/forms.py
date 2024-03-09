from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UpdateUserForm(UserCreationForm):
    first_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'update-form', 'placeholder':'Primeiro nome'}))
    last_name = forms.CharField(label='', max_length=100, widget=forms.TextInput(attrs={'class':'update-form', 'placeholder':'Último nome'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'update-form'
        self.fields['username'].widget.attrs['placeholder'] = 'Nome de usuário'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="spn-form-update"><small>O nome de usuário pode ter até 150 caracteres, letras, digitos, e @/./+/-/_ apenas.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'update-form'
        self.fields['password1'].widget.attrs['placeholder'] = 'Senha'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="spn-form-update small"><li>Sua senha não pode ser muito parecida com suas outras informações pessoais.</li><li>Sua senha deve conter pelo menos 8 caracteres.</li><li>Sua senha não pode ser uma senha comumente usada.</li><li>Sua senha não pode ser inteiramente numérica.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'update-form'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirme a senha'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="spn-form-update"><small>Digite a mesma senha de antes, para verificação.</small></span>'