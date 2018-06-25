from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from programs.models import Program


class StaticSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.2

    def items(self):
        return ['index', 'programs', 'search', 'privacy']

    def location(self, item):
        return reverse(item)


class ProgramSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Program.objects.all()


maps = {
    'static': StaticSitemap,
    'programs': ProgramSitemap,
}
