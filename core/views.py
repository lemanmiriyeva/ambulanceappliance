from django.shortcuts import render
from .models import *
 
def home(request):
    context ={}
 
    context["services"] = Service.objects.all()
    context["works"]=Works.objects.all()
    print(context["services"],context["works"])
         
    return render(request, "index.html", context)


def about(request):
    return render(request,'about.html')


def contact(request):
    return render(request,'contact.html')
