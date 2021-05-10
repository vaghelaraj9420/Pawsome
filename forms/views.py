from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from datetime import datetime
from forms.models import reservation
from forms.models import reservation2

# Create your views here.

def index(request):
    return render(request, "index.html")


def form(request):

    if request.method == 'POST':

        temp_date = datetime.strptime(request.POST['startdate'], "%Y-%m-%d").date()
        date1 = datetime.now().date()
        if temp_date < date1:
            messages.info(request,'Invalid Dates Entered')
            return redirect('form')
            # return redirect('index')
        address = request.POST['address']
        username = request.POST['username']
        noofpets = request.POST['noofpets']
        noofdays = request.POST['noofdays']
        email = request.POST['email']
        phone = request.POST['phone']


        if User.objects.filter(username=username).exists():
            res = reservation(address=address,startdate=temp_date,username=username,noofpets=noofpets,noofdays=noofdays,email=email,phone=phone)
            res.save()
            print('Details submitted successfully')

            return redirect('/')
        else:
            messages.info(request,'Invalid Dates Entered')
            return redirect('form')
        return redirect('/')
    else:
        return render(request,"form.html")




def form2(request):

    if request.method == 'POST':

        temp_date = datetime.strptime(request.POST['startdate'], "%Y-%m-%d").date()
        date1 = datetime.now().date()
        if temp_date < date1:
            messages.info(request,'Invalid Dates Entered')
            return redirect('form2')

        address = request.POST['address']
        username = request.POST['username']
        noofpets = request.POST['noofpets']
        noofdays = request.POST['noofdays']
        email = request.POST['email']
        phone = request.POST['phone']


        if User.objects.filter(username=username).exists():
            res2 = reservation2(address=address,startdate=temp_date,username=username,noofpets=noofpets,noofdays=noofdays,email=email,phone=phone)
            res2.save()
            print('Details submitted successfully')

            return redirect('/')
        else:
            messages.info(request,'Invalid Dates Entered')
            return redirect('form2')
        return redirect('/')
    else:
        return render(request,"form2.html")
