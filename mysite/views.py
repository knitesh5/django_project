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
from mysite.functions.functions import handle_uploaded_file
from .forms import NewUserForm,UploadFileForm
from django.contrib.auth import login,authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth import logout
from django.conf import settings
from django.core.mail import send_mail
import django_excel as excel

import pandas as pd




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
    form = PersonForm(request.POST,request.FILES or None)
    if form.is_valid():
        handle_uploaded_file(request.FILES['file'])
        form.save()
        context["dataset"] = Person.objects.all()
        return redirect("/list_view")
       
    context['form']= form
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
    # emp_id = request.POST['Emp_id']
    name = request.POST['Name']
    email = request.POST['Email']
    job_title = request.POST['Job_title']
    bio = request.POST['Bio']
    file = request.POST['File']
    member = Person.objects.get(emp_id=emp_id)
    member.emp_id = emp_id
    member.name = name
    member.email = email
    member.job_title = job_title
    member.bio = bio
    member.file = file
    member.save()
    return redirect("/list_view")



def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            subject = 'welcome to GFG world'
            message = f'Hi {user.username}, thank you for registering Nitesh website.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email, ]
            send_mail( subject, message, email_from, recipient_list )
            messages.success(request, "Registration successful.Please Login" )
            return redirect("/login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/",user)
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

def logout_view(request):
    logout(request)
    messages.info(request, f"You are now logged out.")
    return redirect("/")


def upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            print("filehandle",filehandle)
            df = pd.read_excel(filehandle)
            print("df",df)
            html = df.to_html()
            return render(request,'upload.html', {'html': html})
    else:
        form = UploadFileForm()
    return render(request,'upload.html',{'form': form})