from django.shortcuts import render, get_object_or_404
from .models import Mineral

# Create your views here.


def mineral_list(request):
    minerals = Mineral.objects.all()
    return render(request, "minerals/mineral_list.html", {"minerals" : minerals})

def mineral_detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    fields = {}
    for field in mineral._meta.fields:
        print(field.name, field.value_to_string(mineral))
        fields.update(
            {field.name : field.value_to_string(mineral)},
        )
    context = {
        "mineral" : mineral,
        "fields" : fields,
    }
    return render(request, "minerals/mineral_detail.html", context)

    