import os
from django.contrib import admin
from django.urls import path, include
from .settings.commons import BASE_DIR
import sys

DEBUG = 'runserver' in sys.argv

if DEBUG == True:
    admin_path_file = os.path.join(BASE_DIR, 'admin_path.txt')

    with open('admin_path.txt', 'r') as file:
        admin_path = file.read().strip()
else:
    admin_path = os.environ.get("ADMIN_PATH")

urlpatterns = [
    path(f"{admin_path}", admin.site.urls),
    path('', include('aplication.urls')),
]
