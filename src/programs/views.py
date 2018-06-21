from django.views.generic import TemplateView, DetailView, ListView

from .models import Program


class Index(TemplateView):
    template_name = "index.html"

    def topics(self):
        return ['STEM', 'Science', 'Engineering']  # TODO
        return Program.objects.only('topic').all()

    def age_groups(self):
        return ['2nd grade', 'third grade', '5-8th grades']  # TODO
        return Program.objects.only('age_group').all()


class ProgramList(ListView):
    model = Program
    template_name = "programs.html"
    context_object_name = 'programs'


class Program(DetailView):
    model = Program
    template_name = "program.html"
