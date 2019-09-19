from collections import OrderedDict
import random 

from django import template

from ..models import Mineral

register = template.Library()

@register.filter(name="random_mineral")
def random_mineral(minerals):
    mineral = random.sample(list(minerals), 1)
    return mineral[0].pk


@register.filter(name="important_top")
def important_top(fields):
    important = OrderedDict(sorted(fields, key=lambda x: len(x[1]), reverse=True))
    return important.items()







