from django.contrib import messages
from django.shortcuts import render,redirect
from PersonalApp.models import contactdb

# Create your views here.
def indexPage(request):
    return render(request,"index.html")

def saveContact(request):
    if request.method == "POST":
        na = request.POST.get("name")
        em = request.POST.get("email")
        me = request.POST.get("message")
        obj = contactdb(Name=na,Email=em,Message=me)
        obj.save()
        messages.success(request, "Message sent successfully..")
        return redirect(indexPage)
