from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from.views import IndexView, AboutView, PortfolioView, ContactView, CommentsView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about', AboutView.as_view(), name='about'),
    path('portfolio', PortfolioView.as_view(), name='portfolio'),
    path('contact', ContactView.as_view(), name='contact'),
    path('ckeditor', include('ckeditor_uploader.urls')),
    path('testimonials', CommentsView.as_view(), name='testimonials')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)