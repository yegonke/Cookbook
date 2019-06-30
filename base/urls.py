from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from rollyourown.seo.admin import register_seo_admin
from django.contrib import admin
from .seo import MyMetadata

urlpatterns = [
    path('', views.index, name='index'),
]

register_seo_admin(admin.site, MyMetadata)


