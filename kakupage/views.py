from django.views.generic import TemplateView

# Create your views here.


class KakuTemplateViwe(TemplateView):
    template_name = 'kakupage/kakupage.html'
