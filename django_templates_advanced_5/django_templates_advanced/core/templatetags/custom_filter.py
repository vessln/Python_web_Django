from django import template

register = template.Library()


@register.filter
def pluralize_word(value):
    toys = []
    suffix = "s"
    for toy in value:
        if value[toy] == 0:
            pass
        elif value[toy] > 1:
            toys.append(f"{value[toy]} {toy}{suffix}")
        else:
            toys.append(f"{value[toy]} {toy}")

    return ", ".join(toys)