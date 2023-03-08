from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Contact
from datetime import datetime


# Create your views here.
def index(request):
    return render(request, 'index.html')

def education(request):
    return render(request, 'education.html')

def contact(request):
    if request.method =='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        contact = Contact(name = name, email = email, phone = phone, desc = desc, date = datetime.today())
        contact.save()
        messages.success(request, "Form successfully submitted")
    return render(request, 'contact.html')
