from django.shortcuts import render
from django.views.generic import ListView
from .models import *
 
#Functional view
# def home(request):
#     context ={}
#     context["services"] = Service.objects.all()[:4:3]
#     context["works"]=Works.objects.filter(title="Work1")
#     print(context["works"])
#     context["abouts"]=About.objects.all()
#     print(context["services"],context["works"])
         
#     return render(request, "index.html", context)

class HomeView(ListView):
    model=Service
    template_name="index.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['services']=Service.objects.all()
        context['works']=Works.objects.all()
        context['abouts']=About.objects.all()
        return context

#Functional view
# def about(request):
#     context={}
#     context["abouts"]=About.objects.all()
#     return render(request,'about.html',context)

#Generic view
class AboutView(ListView):
    model=About
    template_name="about.html"
    context_object_name="abouts"


def contact(request):
    return render(request,'contact.html')
