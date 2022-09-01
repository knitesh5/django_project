from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import InputForm
from django.views.generic import UpdateView
from .models import Person
from .forms import PersonForm
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect


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
    



def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
    # add the dictionary during initialization
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        context["dataset"] = Person.objects.all()
        return redirect("/list_view")
       
    context['form']= form
    # return HttpResponseRedirect("list_view.html")
    return render(request, "person_form.html", context)


def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = Person.objects.all()
         
    return render(request, "list_view.html", context)


def delete(request, emp_id):
    member = Person.objects.get(emp_id=emp_id)
    member.delete()
    return redirect("/list_view")


def edit(request, emp_id):
    mymember = Person.objects.get(emp_id=emp_id)
    template = loader.get_template('edit.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

def updaterecord(request, emp_id):
    name = request.POST['Name']
    email = request.POST['Email']
    job_title = request.POST['Job_title']
    bio = request.POST['Bio']
    member = Person.objects.get(emp_id=emp_id)
    member.emp_id = emp_id
    member.name = name
    member.email = email
    member.job_title = job_title
    member.bio = bio
    member.save()
    return redirect("/list_view")