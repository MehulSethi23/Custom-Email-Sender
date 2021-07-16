from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.contact, name="contact"),
    path('contact', views.contact, name="contact"),
]
