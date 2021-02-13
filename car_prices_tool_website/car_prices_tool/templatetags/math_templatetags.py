from django.template.defaulttags import register


@register.simple_tag
def multiply(value, arg):
    return value * arg
