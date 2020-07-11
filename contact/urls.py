from django.urls import path
from .views import ContactFormView, ContactResultView


app_name = "contact"

urlpatterns = [
    path('contact/', ContactFormView.as_view(), name='contact'),
    # path('kakupage/check/', Contact_confirm.as_viwe(), name='check'),
    path('contact/complete', ContactResultView.as_view(), name='complete')
]
