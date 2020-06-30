from django.urls import path
from .views import KakuTemplateViwe

urlpatterns = [
    path('kakupage/', KakuTemplateViwe.as_view(), name='kakupage-name')
]
