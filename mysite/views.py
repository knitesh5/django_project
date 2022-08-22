from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import InputForm
from django.views.generic import UpdateView
from .models import Person
from .forms import PersonForm


def test(request):
    # return render(request,'index.html')
    return HttpResponse("Hello, world. You're at the good.")

def mock(request):
    # return render(request,'index.html')
    return HttpResponse("Hello, world. You're at the good.mock")


# Create your views here.
def home_view(request):
    return render(request, "home.html")

# Create your views here.
def about(request):
    context ={}
    context['form']= InputForm()
    return render(request, "about.html", context)

# from django.views.generic import CreateView
# from .models import Person



# class PersonUpdateView(UpdateView):
#     model = Person
#     form_class = PersonForm
#     template_name = '/person_update_form.html'
    
from django.views.generic import CreateView
from .models import Person

# class PersonCreateView(CreateView):
#     model = Person
#     fields = ('name', 'email', 'job_title', 'bio')
#     template_name = 'person_form.html'
    

def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = PersonForm(request.POST or None)
    if request.method == 'POST':
        print("form.is_valid",form.is_valid)
        if form.is_valid():
            print("in side")
            form.save()
         
    context['form']= form
    # print("contaxt",context)
    return render(request, "person_form.html", context)