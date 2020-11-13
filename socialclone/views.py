from django.views.generic import TemplateView




class TestPage(TemplateView):
    template_name = 'test.html'


class ThankPage(TemplateView):
    template_name = 'thank.html'


class HomePage(TemplateView):
    template_name = 'index.html'
