from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')

def about(request):
    return render(request, 'accounts/about.html')

def customer(request):
    return render(request, 'accounts/customer.html')

def dash(request):
    return render(request, 'accounts/dashboard.html')