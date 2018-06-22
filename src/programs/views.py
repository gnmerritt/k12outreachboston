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

    def free_programs(self):
        return Program.objects.filter(cost='Free').all().values_list('name', 'id')[:6]


class ProgramList(ListView):
    model = Program
    template_name = "programs.html"
    context_object_name = 'programs'


class SearchList(ProgramList):
    @property
    def topic(self):
        return self.request.GET.get('topic', None)

    @property
    def age_group(self):
        return self.request.GET.get('age', None)

    def get_queryset(self):
        query = Program.objects
        # TODO: probably make this generic via a whitelist & kwargs?
        if self.topic:
            print("added topic filter")
            query = query.filter(topic=self.topic)
        if self.age_group:
            print("added age_group filter")
            query = query.filter(age_group=self.age_group)
        return query.all()


class ProgramView(DetailView):
    model = Program
    template_name = "program.html"
