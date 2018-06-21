from django.views.generic import DetailView, ListView

from .models import Program


class ProgramList(ListView):
    model = Program
    template_name = "programs.html"
    context_object_name = 'programs'


class Program(DetailView):
    model = Program
    template_name = "program.html"
