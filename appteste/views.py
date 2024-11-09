from django.shortcuts import render
from .models import Academia
from django.views.generic import TemplateView


class Home(TemplateView):
    """
    IndexView

    Sobrescrevendo get_context_data para que ele receba a Query com prefetch_related.
    """
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        academias = Academia.objects.prefetch_related('assinantes').all() # reduzindo as queries de forma drástica apenas com prefetch_related
        context['academias'] = academias
        return context