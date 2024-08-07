from bs4 import BeautifulSoup
from django.views.generic import TemplateView, View, CreateView, DeleteView
from .models import Project, ProfileSocialMedia, Profile, Technology, Comment
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import UpdateRegisterForm, UpdatePersonalForm, ProfileUpdateForm, AddSocialMediaForm, AddTestimonialsForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

message_auth_error = 'Você precisa estar autenticado para acessar esta página.'
message_save_data_successfully = "Os seus dados foram atualizados."
message_delete_sucess = "O social media foi excluido"
message_error_owner = "Você não é o proprietário desta rede social"

#Cria uma função que pega o texto gerando no texto dos projetos para adicionar a tag html "<style>" para cada estilo inline, e então adiciona um nonce para todas essas tags.
def process_html_with_nonce(html_content, nonce):
    soup = BeautifulSoup(html_content, 'html.parser')
    styles = []
    
    for tag in soup.find_all(style=True):
        tag_class = tag.get('class', [None])[0]  # Pega a primeira classe, ou None
        if tag_class:
            styles.append(f"{tag.name}.{tag_class} {{{tag['style']}}}")
        else:
            # Se o elemento não tiver uma classe, crie um identificador único
            unique_class = f"unique-class-{id(tag)}"
            tag['class'] = unique_class
            styles.append(f"{tag.name}.{unique_class} {{{tag['style']}}}")
        
        del tag['style']
    
    if styles:
        style_tag = soup.new_tag("style", nonce=nonce)
        style_tag.string = "\n".join(styles)
        if soup.body:
            soup.body.insert(0, style_tag)
        else:
            soup.insert(0, style_tag)
    
    return str(soup)

class IndexView(TemplateView):
    template_name = 'index.html'

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        profile = User.objects.get(is_superuser = True).profile
        context['profile'] = profile
        context['languages'] = Technology.objects.filter(technology_type__name = 'Language')
        context['frameworks_libs'] = Technology.objects.filter(technology_type__name__in=['Framework', 'Lib'])
        return context
    
class PortfolioView(TemplateView):
    template_name = 'portfolio.html'

    def get_context_data(self, **kwargs):
        context = super(PortfolioView, self).get_context_data(**kwargs)
        projects = Project.objects.all()  

        # Resolver o nonce para uma string
        csp_nonce = str(self.request.csp_nonce)

        for project in projects:
            project.text = process_html_with_nonce(project.text, csp_nonce)

        
        context['projects'] = projects
        return context

class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        profile = User.objects.get(is_superuser = True).profile
        context['contacts'] = ProfileSocialMedia.objects.filter(profile = profile.id)
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
        auth_error = 'Nome de usuário ou senha incoreto(s)'
        if user is not None:
            login(request, user)
            messages.success(request, ("You Have Been Logged In"))
            return redirect('profile')
        else:
            return render(request, self.template_name, {'auth_error':auth_error})
        

class ProfilePersonalDataView(TemplateView):
    template_name = 'profile_personal_data.html'

    def get_context_data(self, request, *args, **kwargs):
        current_user = User.objects.get(id=request.user.id)
        profile_user = Profile.objects.get(user__id=request.user.id)
        user_form = UpdatePersonalForm(request.POST or None, request.FILES or None, instance=current_user)
        profile_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=profile_user)
        context = super().get_context_data(*args, **kwargs)
        context['user_form'] = user_form
        context['profile_form'] = profile_form
        return context

    def get(self, request):
        if request.user.is_authenticated:
            return self.render_to_response(self.get_context_data(request))
        else:
            messages.error(request, (message_auth_error), extra_tags='message_auth_error')
            return render(request, self.template_name, {'message_auth_error':message_auth_error})
    
    def post(self, request):
        current_user = User.objects.get(id=request.user.id)
        profile_user = Profile.objects.get(user__id=request.user.id)

        user_form = UpdatePersonalForm(request.POST or None, request.FILES or None, instance=current_user)
        profile_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=profile_user)
        if current_user.is_authenticated:
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
            else:
                return render(request, self.template_name, {'user_form': user_form, 'profile_form':profile_form})
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
        if request.user.is_authenticated:
            return self.render_to_response(self.get_context_data(request))
        else:
            messages.error(request, (message_auth_error), extra_tags='message_auth_error')
            return render(request, self.template_name, {'message_auth_error':message_auth_error})
    
    def post(self, request):
        current_user = User.objects.get(id=request.user.id)
        form = UpdateRegisterForm(request.POST, instance=current_user)
        if current_user.is_authenticated:
            if form.is_valid():
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
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            messages.error(request, (message_auth_error), extra_tags='message_auth_error')
            return render(request, self.template_name, {'message_auth_error':message_auth_error})

class AddSocialMediaView(CreateView):
    template_name = 'add_social_media.html'

    def get_form_kwargs(self):
        user = self.request.user
        profile_user = get_object_or_404(Profile, user=user)
        kwargs = super(AddSocialMediaView, self).get_form_kwargs()
        kwargs.update({'profile': profile_user})

    def post(self, request):
        if request.user.is_authenticated:
            profile_user = Profile.objects.get(user=request.user)
            form = AddSocialMediaForm(data=request.POST or None, profile=profile_user)
            if form.is_valid():
                social_media = form.save(commit=False)
                social_media.profile = profile_user
                social_media.save()
                messages.success(request, "Os seus dados foram atualizados.", extra_tags='message_save_data_successfully')
                return render(request, self.template_name, {'message_save_data_successfully': message_save_data_successfully, 'form': form})
            else:
                return render(request, self.template_name, {'form': form})
        else:
            messages.error(request, message_auth_error, extra_tags='message_auth_error')
        


    def get(self, request):
        if request.user.is_authenticated:
            profile_user = get_object_or_404(Profile, user=request.user)
            form = AddSocialMediaForm(data=request.GET or None, profile=profile_user)
            return render(request, self.template_name, {'form':form})
        else:
            messages.error(request, (message_auth_error), extra_tags='message_auth_error')
            return render(request, self.template_name, {'message_auth_error':message_auth_error})
        
class TestimonialsView(TemplateView):
    template_name = 'testimonials.html'

    def get(self, request):
        if request.user.is_authenticated:
            profile_user = get_object_or_404(Profile, user=request.user)
            testimonial = profile_user.comments.first()
            form = AddTestimonialsForm(data=request.GET or None, profile=profile_user, instance=testimonial)
            return render(request, self.template_name, {'form':form})
        else:
            messages.error(request, (message_auth_error), extra_tags='message_auth_error')
            return render(request, self.template_name, {'message_auth_error':message_auth_error})

    def post(self, request):
        if request.user.is_authenticated:
            profile_user = Profile.objects.get(user=request.user)
            testimonial = profile_user.comments.first()
            form = AddTestimonialsForm(data=request.POST or None, profile=profile_user, instance=testimonial)
            if form.is_valid():
                testimonial = form.save(commit=False)
                testimonial.profile = profile_user
                testimonial.save()
                messages.success(request, "Os seus dados foram atualizados.", extra_tags='message_save_data_successfully')
                return render(request, self.template_name, {'message_save_data_successfully': message_save_data_successfully, 'form': form})
            else:
                messages.error(request, (message_auth_error), extra_tags='message_auth_error')
                return render(request, self.template_name, {'form': form}) 

        else:
            messages.error(request, (message_auth_error), extra_tags='message_auth_error')
            return render(request, self.template_name, {'message_auth_error':message_auth_error})

class DeleteSocialsView(DeleteView):
    template_name = 'profilesocialmedia_confirm_delete.html'
    queryset = ProfileSocialMedia.objects.all()

    def post(self, request, pk):
        
        if request.user.is_authenticated:
            social = get_object_or_404(ProfileSocialMedia, id=pk)
            if request.user.username == social.profile.user.username:
                social.delete()
                messages.success(request, message_delete_sucess)
                return redirect('socials_edit')

            else:
                messages.error(request, message_error_owner)
        else:
            messages.error(request, (message_auth_error), extra_tags='message_auth_error')
        return redirect('socials_edit')

class EditSocialsView(TemplateView):
    template_name = "delete_socials.html"

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            messages.error(request, (message_auth_error), extra_tags='message_auth_error')
            return render(request, self.template_name, {'message_auth_error':message_auth_error})

class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, ("You have been logged out"))
        return redirect('login')