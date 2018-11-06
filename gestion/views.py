from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from gestion.models import Profesor

def index(request):
    return render(request, 'template.html')

class VerProfesor(DetailView):
    
    template_name = 'profesores/ver.html'
    model = Profesor
    
    def get_context_data(self, **kwargs):
        context = super(VerProfesorlView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_context_object_name(self):
        return "profesor"