from django.views.generic import TemplateView
# Create your views here.


class HomeTemplateViwe(TemplateView):
    template_name = 'home/home.html'
