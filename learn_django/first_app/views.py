from django.shortcuts import render
from .models import Chaia_Variety
from django.shortcuts import get_object_or_404

# Create your views here.
def all_chai(request):
    all_chais = Chaia_Variety.objects.all()

    print(all_chais)
    print(request,"Request")
    return render(request, "first_app/first_app.html",{'chais':all_chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(Chaia_Variety,pk=chai_id)
    return render(request, "first_app/chai_detail.html",{'chai':chai})