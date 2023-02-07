from django.shortcuts import render,redirect
from django.views.generic import ListView,FormView
from django.urls import reverse_lazy
from .models import *
from .forms import *

#Functional view
# def home(request):
#     context ={}
#     context["services"] = Service.objects.all()[:4:3]
#     context["works"]=Works.objects.filter(title="Work1")
#     print(context["works"])
#     context["abouts"]=About.objects.all()
#     print(context["services"],context["works"])
         
#     return render(request, "index.html", context)

class HomeView(ListView,FormView):
    model=Service
    template_name="index.html"
    form_class=QuoteForm
    
    def get_success_url(self):
        return self.request.path


    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)

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
    form=ContactForm()
    print(request.POST)
    if request.method == 'POST':
        form=ContactForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy("home"))
    context={
        'form':form
    }

    return render(request,'contact.html',context)

