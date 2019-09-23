import re
from django.shortcuts import render, get_object_or_404

from .models import Mineral


def mineral_list(request):
    """main list view displaying all minerals in database"""
    minerals = Mineral.objects.all()
    pagin_set = sorted(set(map(lambda x: x.name[0].lower(), minerals)))
    pattern = re.compile(r'[a-z]')
    valid_pagin_list = [x for x in pagin_set if pattern.match(x)]
    context = {
        "minerals": minerals,
        "pagin_list": valid_pagin_list,
    }
    return render(request, "minerals/mineral_list.html", context)


def mineral_detail(request, pk):
    """detail view displaying all available attributes of passed in 
    mineral
    """
    mineral = get_object_or_404(Mineral, pk=pk)
    minerals = Mineral.objects.all()
    fields = mineral.fields_lower

    context = {
        "mineral": mineral,
        "fields": fields,
        "minerals": minerals,
    }
    return render(request, "minerals/mineral_detail.html", context)
