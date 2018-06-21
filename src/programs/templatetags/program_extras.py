from django import template

register = template.Library()


@register.inclusion_tag('fragments/info.html')
def card(title, text, *args, **kwargs):
    return {
        'title': title, 'text': text,  # required
        't2': kwargs.get('t2', None),
        'link': kwargs.get('link', False)
    }
