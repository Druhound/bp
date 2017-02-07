from django import template

from app.slider.models import Slider

register = template.Library()

@register.inclusion_tag("slider/slider_tag.html")
def ShowSlider(group_slug):
    context = {}

    return context