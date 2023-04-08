from django import template
from datetime import datetime
register = template.Library()

@register.filter(name="addstr")
def addstr(arg1,arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)

@register.filter(name="get_attribute")
def get_attribute(obj,prop):
    return getattr(obj,prop)

@register.filter("get_value")
def get_value(obj, prop):
    return obj[prop]

@register.filter(name="date_format")
def date_format(arg):
    arg = datetime.strptime(arg, '%Y-%m-%d').date()
    return arg.strftime('%B %d, %Y')


@register.filter(name="monthYear_format")
def date_format(arg):
    arg = datetime.strptime(arg, '%Y-%m').date()
    return arg.strftime('%B %Y')
