import random 

from django import template

from ..models import Mineral

register = template.Library()

@register.filter(name="random_mineral")
def random_mineral(minerals):
    mineral = random.sample(list(minerals), 1)
    return mineral[0].pk

