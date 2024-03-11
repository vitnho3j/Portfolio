from django.views.generic import TemplateView, View
from .models import Project, ProfileSocialMedia, Profile, Technology, Comment
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import UpdateRegisterForm, UpdatePersonalForm
from django.contrib.auth.models import User


class IndexView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['profile'] = Profile.objects.get(id = 1)
        context['languages'] = Technology.objects.filter(technology_type__name = 'Language')
        context['frameworks_libs'] = Technology.objects.filter(technology_type__name__in=['Framework', 'Lib'])
        return context
    
class PortfolioView(TemplateView):
    template_name = 'portfolio.html'

    def get_context_data(self, **kwargs):
        context = super(PortfolioView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.all()
        return context


class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['contacts'] = ProfileSocialMedia.objects.filter(profile = 1)
        return context
    
class CommentsView(TemplateView):
    template_name = 'comments.html'

    def get_context_data(self, **kwargs):
        context = super(CommentsView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        return context


class LoginView(TemplateView):
    template_name="login.html"
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You Have Been Logged In"))
            return redirect('index')
        else:
            messages.error(request, ("Your username or password is incorrect, please try again"))
            return redirect('login')
        

class ProfilePersonalDataView(TemplateView):
    template_name = 'profile_personal_data.html'

    def get_context_data(self, request, *args, **kwargs):
        current_user = User.objects.get(id=request.user.id)
        form = UpdatePersonalForm(instance=current_user)
        context = super().get_context_data(*args, **kwargs)
        context['form'] = form
        context['current_user'] = current_user
        return context

    def get(self, request):
        message_auth_error = 'Você precisa estar autenticado para acessar esta página.'
        if request.user.is_authenticated:
            return self.render_to_response(self.get_context_data(request))
        else:
            messages.error(request, (message_auth_error), extra_tags='message_auth_error')
            return render(request, self.template_name, {'message_auth_error':message_auth_error})
    
    def post(self, request):
        message_auth_error = 'Você precisa estar autenticado para acessar esta página.'
        current_user = User.objects.get(id=request.user.id)
        form = UpdatePersonalForm(request.POST, instance=current_user)
        message_save_data_successfully = "Os seus dados foram atualizados."
        if current_user.is_authenticated:
            if form.is_valid():
                form.save()
            else:
                return render(request, self.template_name, {'form': form})
        else:
            messages.error(request, (message_auth_error), extra_tags='message_auth_error')
        messages.success(request, (message_save_data_successfully), extra_tags='message_save_data_successfully')
        return render(request, self.template_name, {'message_save_data_successfully':message_save_data_successfully})

class ProfileRegisterDataView(TemplateView):
    template_name = 'profile_register_data.html'

    def get_context_data(self, request, *args, **kwargs):
        current_user = User.objects.get(id=request.user.id)
        form = UpdateRegisterForm(instance=current_user)
        context = super().get_context_data(*args, **kwargs)
        context['form'] = form
        context['current_user'] = current_user
        return context

    def get(self, request):
        message_auth_error = 'Você precisa estar autenticado para acessar esta página.'
        if request.user.is_authenticated:
            return self.render_to_response(self.get_context_data(request))
        else:
            messages.error(request, (message_auth_error), extra_tags='message_auth_error')
            return render(request, self.template_name, {'message_auth_error':message_auth_error})
    
    def post(self, request):
        message_auth_error = 'Você precisa estar autenticado para acessar esta página.'
        current_user = User.objects.get(id=request.user.id)
        form = UpdateRegisterForm(request.POST, instance=current_user)
        message_save_data_successfully = "Os seus dados foram atualizados."
        if current_user.is_authenticated:
            if form.is_valid():
                if form.cleaned_data['username'] == current_user.username:
                    form.fields['username'].validators = []
                form.save()
            else:
                return render(request, self.template_name, {'form': form})
        else:
            messages.error(request, (message_auth_error), extra_tags='message_auth_error')
        login(request, current_user)
        messages.success(request, (message_save_data_successfully), extra_tags='message_save_data_successfully')
        return render(request, self.template_name, {'message_save_data_successfully':message_save_data_successfully})

class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get(self, request):
        message_auth_error = 'Você precisa estar autenticado para acessar esta página, portanto, será redirecionado para a página inicial após 5 segundos.'
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            messages.error(request, (message_auth_error), extra_tags='message_auth_error')
            return render(request, self.template_name, {'message_auth_error':message_auth_error})
    
    # def post(self, request):
    #     current_user = User.objects.get(id=request.user.id)
    #     form = UpdateUserForm(request.POST, instance=current_user)
    #     if current_user.is_authenticated:
    #         if form.is_valid():
    #             form.save()
    #             messages.success(request, ("Os seus dados foram atualizados."))
    #         else:
    #             return render(request, 'profile.html', {'form': form})
    #     else:
    #         messages.error(request, ("Você precisa estar autenticado para acessar esta página."))
    #     print(form.is_valid())
    #     print(form)
    #     return redirect('index')

class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, ("You have been logged out"))
        return redirect('login')