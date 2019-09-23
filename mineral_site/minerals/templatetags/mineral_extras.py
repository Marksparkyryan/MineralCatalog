from collections import OrderedDict
import random

from django import template

from ..models import Mineral

register = template.Library()


@register.filter(name="random_mineral")
def random_mineral(minerals):
    """retrieve and return random mineral pk from database"""
    mineral = random.sample(list(minerals), 1)
    return mineral[0].pk


@register.filter(name="important_top")
def important_top(fields):
    """takes in fields and field values and sorts by field value length"""
    important = OrderedDict(
        sorted(fields, key=lambda x: len(x[1]), reverse=True)
    )
    return important.items()


@register.filter(name="first_letter")
def first_letter(mineral):
    """returns first letter of passed in mineral name as lowercase"""
    return mineral.name[0].lower()


@register.filter(name="display_fields")
def display_fields(fields):
    """returns only fields that are meant to be displayed in text in 
    detail
    """
    display_fields = {}
    for key, value in fields:
        if key not in ["id", "name", "image filename", "image caption"]:
            display_fields.update({key: value})
    return display_fields.items()
