from django import template
from datetime import datetime
register = template.Library()


@register.filter(name="date_format")
def date_format(arg):
    arg = datetime.strptime(arg, '%Y-%m-%d').date()
    return arg.strftime('%B %d, %Y')
