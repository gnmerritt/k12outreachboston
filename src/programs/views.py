from typing import Optional
from django.views.generic import TemplateView, DetailView, ListView
from django.contrib.postgres.search import SearchVector

from .models import Program


def unique(l, count):
    s = set(l)
    return list(s)[:count]


class Index(TemplateView):
    template_name = "index.html"

    def topics(self):
        topics = Program.objects.all().values_list('topic', flat=True)
        return unique([s.strip() for t in topics for s in t.split(',')], 6)

    def age_groups(self):
        return unique(Program.objects.all().values_list('age_group', flat=True)[:], 6)

    def free_programs(self):
        return Program.objects.filter(cost='Free').all().values_list('name', 'id')[:6]


class ProgramList(ListView):
    model = Program
    template_name = "programs.html"
    context_object_name = 'programs'


class SearchList(ProgramList):
    SEARCHABLE = [
        'name', 'topic', 'date', 'description', 'location', 'age_group', 'cost'
    ]

    def arg(self, arg: str) -> Optional[str]:
        if self.request.method == 'GET':
            return self.request.GET.get(arg, None)

    @property
    def topic(self) -> Optional[str]:
        return self.arg('topic')

    @property
    def age_group(self) -> Optional[str]:
        return self.arg('age')

    @property
    def search(self) -> Optional[str]:
        return self.arg('q')

    def get_queryset(self):
        query = Program.objects
        # TODO: probably make this generic via a whitelist & kwargs?
        if self.search:
            query = query.annotate(search=SearchVector(*self.SEARCHABLE)) \
                .filter(search=self.search)
        if self.topic:
            query = query.filter(topic__icontains=self.topic)
        if self.age_group:
            query = query.filter(age_group__icontains=self.age_group)
        return query.all()


class ProgramView(DetailView):
    model = Program
    template_name = "program.html"
