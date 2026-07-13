from django.shortcuts import render

# Create your views here.
def all_chai(request):
    print(request,"Request")
    return render(request, "first_app/first_app.html")