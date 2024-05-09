from django.shortcuts import render,HttpResponseRedirect
from django.db.models import Q
from .models import Employee

def homePage(Request):
    data = Employee.objects.all()
    return render(Request,"index.html",{'data':data})

def addPage(Request):
    if(Request.method=="POST"):
        e = Employee()
        e.name = Request.POST.get("name")
        e.email = Request.POST.get("email")
        e.phone = Request.POST.get("phone")
        e.dsg = Request.POST.get("dsg")
        e.salary = Request.POST.get("salary")
        e.city = Request.POST.get("city")
        e.state = Request.POST.get("state")
        e.save()
        return HttpResponseRedirect("/")
    return render(Request,"add.html")


def deleteRecord(Request,id):
    try:
        data = Employee.objects.get(id=id)
        data.delete()
    except:
        pass
    return HttpResponseRedirect("/")

def editRecord(Request,id):
    try:
        data = Employee.objects.get(id=id)
        if (Request.method=="POST"):
            data.name = Request.POST.get("name")
            data.email = Request.POST.get("email")
            data.phone = Request.POST.get("phone")
            data.dsg = Request.POST.get("dsg")
            data.city = Request.POST.get("city")
            data.state = Request.POST.get("state")
            data.save()
            return HttpResponseRedirect("/")
        return render(Request,"edit.html",{'data':data})
    except:
        pass
    return HttpResponseRedirect("/")

def searchPage(Request):
    if(Request.method=="POST"):
        search = Request.POST.get("search")
        data = Employee.objects.filter(Q
        (name__icontains=search)|Q
        (city__icontains=search)|Q
        (state__icontains=search)|Q
        (email__icontains=search)|Q
        (phone__icontains=search)|Q
        (dsg=search))
        return render(Request,"index.html",{'data':data})
    else:
        return HttpResponseRedirect("/")

    