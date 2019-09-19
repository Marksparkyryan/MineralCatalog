from django.shortcuts import render, get_object_or_404
from .models import Mineral

# Create your views here.


def mineral_list(request):
    minerals = Mineral.objects.all()
    return render(request, "minerals/mineral_list.html", {"minerals" : minerals})

def mineral_detail(request, pk):
    mineral = get_object_or_404(Mineral, pk=pk)
    minerals = Mineral.objects.all()
    fields = {}
    for field in mineral._meta.fields[4:]:
        fields.update(
            {field.name.replace("_", " ") : field.value_to_string(mineral)},
        )
    context = {
        "mineral" : mineral,
        "fields" : fields,
        "minerals" : minerals,
    }
    return render(request, "minerals/mineral_detail.html", context)

    