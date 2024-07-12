from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from portfolio.settings.commons import BASE_DIR
import os
import sys
from.views import IndexView, AboutView, PortfolioView, ContactView, CommentsView, LoginView, LogoutView, ProfileView, DeleteSocialsView, ProfileRegisterDataView, ProfilePersonalDataView, AddSocialMediaView, TestimonialsView, EditSocialsView

DEBUG = 'runserver' in sys.argv

if DEBUG == True:
    login_path_file = os.path.join(BASE_DIR, 'login_path.txt')

    with open('login_path.txt', 'r') as file:
        login_path = file.read().strip()
else:
    login_path = os.environ.get("LOGIN_PATH")


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about', AboutView.as_view(), name='about'),
    path('portfolio', PortfolioView.as_view(), name='portfolio'),
    path('contact', ContactView.as_view(), name='contact'),
    path('testimonials', CommentsView.as_view(), name='testimonials'),
    path(f'{login_path}', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('profile/register/data', ProfileRegisterDataView.as_view(), name='register_data'),
    path('profile/personal/data', ProfilePersonalDataView.as_view(), name='personal_data'),
    path('profile/social/add', AddSocialMediaView.as_view(), name='social_add'),
    path('profile/testimonials', TestimonialsView.as_view(), name='testimonials_add'),
    path('profile/social/edit', EditSocialsView.as_view(), name='socials_edit'),
    path('profile/social/delete/<int:pk>', DeleteSocialsView.as_view(), name='socials_delete'),

    #CKEditor
    path("ckeditor5/", include("django_ckeditor_5.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)