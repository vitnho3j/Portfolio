from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from.views import IndexView, AboutView, PortfolioView, ContactView, CommentsView, LoginView, LogoutView, ProfileView, EditSocialsView, ProfileRegisterDataView, ProfilePersonalDataView, AddSocialMediaView, TestimonialsView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about', AboutView.as_view(), name='about'),
    path('portfolio', PortfolioView.as_view(), name='portfolio'),
    path('contact', ContactView.as_view(), name='contact'),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('testimonials', CommentsView.as_view(), name='testimonials'),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('profile/register/data', ProfileRegisterDataView.as_view(), name='register_data'),
    path('profile/personal/data', ProfilePersonalDataView.as_view(), name='personal_data'),
    path('profile/social/add', AddSocialMediaView.as_view(), name='social_add'),
    path('profile/testimonials', TestimonialsView.as_view(), name='testimonials_add'),
    path('profile/social/edit', EditSocialsView.as_view(), name='socials_edit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)