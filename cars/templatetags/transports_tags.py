from django import template
from cars.models import CategoryTransport


register = template.Library()


@register.simple_tag(name='categories_list')
def get_categories():
    return CategoryTransport.objects.all()