from django.shortcuts import render
from .models import Chaia_Variety, Store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarietyForm

# Create your views here.
def all_chai(request):
    all_chais = Chaia_Variety.objects.all()

    print(all_chais)
    print(request,"Request")
    return render(request, "first_app/first_app.html",{'chais':all_chais})

def chai_detail(request, chai_id):
    chai = get_object_or_404(Chaia_Variety,pk=chai_id)
    return render(request, "first_app/chai_detail.html",{'chai':chai})

def chai_stores(request):
    stores = None
    selected_chai = None
    if request.method == "POST":
        form = ChaiVarietyForm(request.POST)
        if form.is_valid():
            selected_chai = form.cleaned_data['chai_variety']
            stores = Store.objects.filter(chai_varities=selected_chai)
    else:
        form = ChaiVarietyForm()
    return render(request, "first_app/chai_stores.html", {
        'form': form,
        'stores': stores,
        'selected_chai': selected_chai
    })