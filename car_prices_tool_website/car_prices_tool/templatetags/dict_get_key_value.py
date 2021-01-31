from django.template.defaulttags import register


@register.simple_tag
def get_item(dictionary, key, index=0):
    return dictionary.get(key)[index]
