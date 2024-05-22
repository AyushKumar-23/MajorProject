from django import template

register = template.Library()

@register.filter
def leading_zero(value):
    try:
        return f"{int(value):02}"
    except (ValueError, TypeError):
        return value
