from django.urls import path
from . import views


app_name = "kakupage"

urlpatterns = [
    # path('kakupage/', views.index, name='kakupage'),
    path('kakupage/', views.contact_form, name='kaku-contact'),
    # path('kakupage/check/', Contact_confirm.as_viwe(), name='check'),
    path('kakupage/check/complete/', views.complete, name='complete')

]
