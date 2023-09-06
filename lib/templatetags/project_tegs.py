from django import template
from django.conf import settings

register = template.Library()

@register.simple_tag()
def media(path):
    return settings.MEDIA_URL + str(path)


@register.simple_tag(name='eval')
def eval_numbers(*args):
    eval_string = ''
    for el in args:
        eval_string += str(el)
    return eval(eval_string)


@register.inclusion_tag('pagination.html', takes_context=True)
def pagination(context):
    data = context.request.GET
    params = ''
    if data:
        for key in data:
            if key == 'page': continue
            params += '&'+key+'='+data[key]
    return {
        'params': params,
        'page_obj': context['page_obj']
    }
