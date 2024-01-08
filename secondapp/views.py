from django.shortcuts import render

# Create your views here.

def hellofirst(request):
    return render(request,'helloworld1.html')

def hellosecond(request):
    return render(request,'helloworld2.html')
