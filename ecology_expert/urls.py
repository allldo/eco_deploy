
from django.contrib import admin
from django.urls import path
from main.views import start, contact, service, projects, aboutUs, Taldyk, Pavlodar, Atyrau, review

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', start, name='startPage'),
    path('contacts/', contact, name='contacts'),
    path('service/', service, name='services'),
    path('projects/', projects, name='projects'),
    path('aboutUs/', aboutUs, name='about'),
    path('Taldykorgan/', Taldyk, name='taldyk'),
    path('Pavlodar/', Pavlodar, name='Pavlodar'),
    path('Atyrau/', Atyrau, name='Atyrau'),
    path('reviews/', review, name='reviews'),
]
