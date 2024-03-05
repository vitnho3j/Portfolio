from typing import Any
from django.views.generic import TemplateView, View
from .models import Project, ProfileSocialMedia, Profile, Technology, Comment
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect
from .models import User


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


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, ("You have been logged out"))
        return redirect('login')