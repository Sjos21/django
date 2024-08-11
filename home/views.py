from django.shortcuts import render, HttpResponse 
from datetime import datetime
from home.models import Contact
# from django.contrib.messages import constants as messages
from django.contrib import messages
# Create your views here.
def index(request):
    context={
        'variable1':"this is sent",
        'variable2':"this is sent once again"
    }
    messages.success(request, "this is a test message")
    return render(request, 'index.html',context)
    # return HttpResponse("this is a homepage")
def about(request):
    return render(request, 'about.html')
    # return HttpResponse("this is about page")
def services(request):
    return render(request, 'services.html')
    # return HttpResponse("this is services page")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your form has been submitted")
    return render(request, 'contact.html')
    