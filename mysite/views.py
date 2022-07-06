from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import InputForm

def test(request):
    # return render(request,'index.html')
    return HttpResponse("Hello, world. You're at the good.")

def mock(request):
    # return render(request,'index.html')
    return HttpResponse("Hello, world. You're at the good.mock")


 
# Create your views here.
def home_view(request):
    context ={}
    context['form']= InputForm()
    print("data ",context)
    print("request   ",request)
    return render(request, "home.html", context)