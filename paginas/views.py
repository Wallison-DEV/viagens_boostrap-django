from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'modelo.html'
class SobreView(TemplateView):
    template_name = 'sobre.html'
