from django import template
from datetime import datetime
register = template.Library()


@register.filter(name="date_format")
def date_format(arg):
    arg = datetime.strptime(arg, '%Y-%m-%d').date()
    return arg.strftime('%B %d, %Y')

@register.filter(name="addstr")
def addstr(arg1,arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)

@register.filter("get_value")
def get_value(obj, prop):
    if obj[prop]:
        return obj[prop]
    print("FAIL")


@register.filter(name="get_attribute")
def get_attribute(obj, prop):
    return getattr(obj, prop)

@register.filter("hours_minutes")
def hours_minutes(obj):
    hours = obj // 60
    minutes = obj % 60
    return f"{hours} Hour(s) {minutes} Minutes"
