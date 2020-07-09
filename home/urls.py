from django.urls import path
from .views import HomeTemplateViwe

urlpatterns = [
    path('', HomeTemplateViwe.as_view(), name='home-name'),
    path('contact/', HomeTemplateViwe.as_view(), name='contact')
]
