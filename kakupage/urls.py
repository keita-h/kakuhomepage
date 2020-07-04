from django.urls import path
from . import views


app_name = "kakupage"

urlpatterns = [
    # path('kakupage/', views.index, name='kakupage'),
    path('kakupage/', views.contact_form, name='kaku-contact'),
    path('kakupage/complete/', views.complete, name='complete')

]
