from django import template

register = template.Library()


@register.filter(name="addstr")
def addstr(arg1,arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)

@register.filter
def get_attribute(obj,prop):
    return getattr(obj,prop)


@register.filter
def get_value(obj, prop):
    return obj[prop]
