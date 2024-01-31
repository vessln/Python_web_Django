from django import template

register = template.Library()


# return context
@register.inclusion_tag("tags/user_profile.html", takes_context=True)
def show_auth_user(context):
    user = context.request.user
    if user.is_authenticated:
        user_names = f"{user.username} {user.last_name[0]}."

    else:
        user_names = ""

    return {
        "user_names": user_names,
    }
