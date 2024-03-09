from django.views.generic import TemplateView, View
from .models import Project, ProfileSocialMedia, Profile, Technology, Comment
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import UpdateUserForm
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

class ProfileView(TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, request, **kwargs):
        current_user = User.objects.get(id=request.user.id)
        form = UpdateUserForm(instance=current_user)
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['form'] = form
        context['current_user'] = current_user
        return context


    def get(self, request):
        if request.user.is_authenticated:
            return self.render_to_response(self.get_context_data(request))
        else:
            messages.error(request, ("Você precisa estar autenticado para acessar esta página."))
            return redirect('index')
    
    def post(self, request):
        current_user = User.objects.get(id=request.user.id)
        form = UpdateUserForm(request.POST, instance=current_user)
        if current_user.is_authenticated:
            if form.is_valid():
                form.save()
                messages.success(request, ("Os seus dados foram atualizados."))
            else:
                return render(request, 'profile.html', {'form': form})
        else:
            messages.error(request, ("Você precisa estar autenticado para acessar esta página."))
        print(form.is_valid())
        print(form)
        return redirect('index')

class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, ("You have been logged out"))
        return redirect('login')