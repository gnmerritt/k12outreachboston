from django.views.generic import TemplateView, DetailView, ListView

from .models import Program


def unique(l, count):
    s = set(l)
    return list(s)[:count]


class Index(TemplateView):
    template_name = "index.html"

    def topics(self):
        return unique(Program.objects.all().values_list('topic', flat=True)[:], 6)

    def age_groups(self):
        return unique(Program.objects.all().values_list('age_group', flat=True)[:], 6)


class ProgramList(ListView):
    model = Program
    template_name = "programs.html"
    context_object_name = 'programs'


class ProgramView(DetailView):
    model = Program
    template_name = "program.html"
