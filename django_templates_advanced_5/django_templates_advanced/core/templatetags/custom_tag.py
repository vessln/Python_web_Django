from datetime import datetime

from django import template

register = template.Library()


# expects to return HTML string to visualize:
@register.simple_tag
def current_time_now():

    return datetime.now().strftime("%d/%m/%Y %H:%M")

