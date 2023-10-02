from django import template

register = template.Library()


@register.filter
def split(value, delimiter):
    edited_str = value[:delimiter]
    return f'{edited_str}...'


@register.filter
def mymedia(val):
    if val:
        return f'/media/{val}'
    else:
        return '#'
