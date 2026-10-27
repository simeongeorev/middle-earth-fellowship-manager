from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def power_stars(power: int):
    if power <= 20:
        filled_stars = 1
    elif power <= 40:
        filled_stars = 2
    elif power <= 60:
        filled_stars = 3
    elif power <= 80:
        filled_stars = 4
    else:
        filled_stars = 5

    empty_stars = 5 - filled_stars

    return mark_safe(
        f'<span class="power-stars" title="Combat power: {power}">'
        f'<span class="text-gold">{"★" * filled_stars}</span>'
        f'<span class="text-muted">{"☆" * empty_stars}</span>'
        f'</span>'
    )
