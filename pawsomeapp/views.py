#pip install wolframalpha
#pip install wikipedia
#pip install pyttsx3
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Pets
from .models import pList
from .models import ppList
from .models import daycare
from .models import caretaker
from .models import Contact
from .models import Orders
from .models import OrderUpdate
from .models import vet
from forms.models import reservation2
import json
import wolframalpha
import wikipedia
import webbrowser
import pyttsx3
from django.views.decorators.csrf import csrf_exempt
from Paytm import Checksum
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from django.contrib.auth import authenticate

# Create your views here.
MERCHANT_KEY = ''

def index(request):

    pets = Pets.objects.all()

    return render(request, "index.html", {'pets' : pets})

def sendanemail(request):
    if request.method == 'POST':
        to = request.POST.get('toemail')
        fromemail = request.POST.get('fromemail')
        EMAIL_HOST_PASSWORD = request.POST.get('password')
        content = request.POST.get('content')
        print(to,fromemail,content)
        send_mail(

            "testing",                      # subject

            content,                        # msg

            fromemail,                      # from email

            [to],                           # recipient's list

            fail_silently=False,
        )
        return render(request, 'email.html', {'title':'send an email'})
    else:
        return render(request, 'email.html', {'title':'send an email'})

def buy12(request):
    return render(request, "buy12.html")

def sign12(request):
    return render(request, "sign12.html")

def login12(request):
    return render(request, "login12.html")

def faq(request):
    return render(request, "faq.html")

def vets(request):
    veterinary = vet.objects.all()
    print(veterinary)
    return render(request, "vet.html", {'veterinary': veterinary})


def PetList(request):

    pLists = pList.objects.all()
    return render(request, "PetList.html", {'pLists': pLists})


def PetProductList(request):

    ppLists = ppList.objects.all()
    return render(request, "PetProductList.html", {'ppLists': ppLists})

def DayCare(request):

    daycares = daycare.objects.all()
    return render(request, "DayCare.html", {'daycares' : daycares})

def Caretaker(request):

    caretakers = caretaker.objects.all()
    return render(request,"Caretaker.html", {'caretakers': caretakers})


def caretakersignup(request):

    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        img = request.POST['img']
        address = request.POST['adds']
        rate = request.POST['rate']
        contact = request.POST['contact']
        location = request.POST['location']
        experience = request.POST['experience']
        is_staff = False
        is_active=True
        is_superuser=False

        if password1 == password2:

            if caretaker.objects.filter(username=username).exists():

                messages.info(request,'Username taken')
                return redirect('caretakersignup')
            elif caretaker.objects.filter(email=email).exists():

                messages.info(request,'email taken')
                return redirect('caretakersignup')
            else:
                caretakers = caretaker.objects.create(name=name,username=username,email=email,password=password1,img=img,location=location,adds=address,rate=rate,contact=contact,experience=experience,is_staff=is_staff,is_active=is_active,is_superuser=is_superuser)
                caretakers.save()
                print('caretaker created')
                return redirect('caretakerlogin')
        else:
            messages.info(request,'Password not matching')
            return redirect('caretakersignup')
        return redirect('/')
    else:

        return render(request, 'caretakersignup.html')


def caretakerlogin(request):
    if request.method== 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        caretakers = auth.authenticate(username=username,password=password)

        if caretakers is not None:
            auth.login(request, caretakers)
            request.session['username']=username             # setting the session variable
            return redirect('cportal')
        else:
            messages.info(request,'invalid credentials')
            return redirect('caretakerlogin')

    else:
        return render(request,'caretakerlogin.html')


def caretakerlogout(request):
    auth.logout(request)
    return redirect('/')


def cportal(request):
    username1 = request.session['username']                    # getting the session variable
    caretakers = caretaker.objects.filter(username=username1)
    print(caretakers)
    return render(request,"cportal.html", {'caretaker': caretakers[0]})

def customerdeals(request):

    customerdeals = reservation2.objects.all()
    return render(request, "customer-deals.html", {'customerdeals': customerdeals})


def productView(request, myid):
    product=ppList.objects.filter(id=myid)
    print(product)
    return render(request, "prodView.html", {'product':product[0]})


def contactbreeder(request, myid):
    petbreeder=pList.objects.filter(id=myid)
    print(petbreeder)
    return render(request, "contactbreeder.html", {'petbreeder':petbreeder[0]})

def contact(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        return redirect('/')
    return render(request, 'contact.html')


def checkout(request):
    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')

        order = Orders(items_json= items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code, phone=phone, amount=amount)
        order.save()
        update = OrderUpdate(order_id=order.order_id, update_desc="The order has been placed")
        update.save()

        thank=True
        id = order.order_id

        #request paytm to transfer the amount to your account after payment by user
        param_dict={

                'MID': '',
                'ORDER_ID': str(order.order_id),
                'TXN_AMOUNT': amount,
                'CUST_ID': email,
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://127.0.0.1:8080/handlerequest/',

        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return  render(request, 'paytm.html', {'param_dict': param_dict})

    return render(request, 'checkout.html')




@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')
        else:
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'paymentstatus.html', {'response': response_dict})



def chatbot(request):
    return render(request, "chatbot.html")

def bot_search(request):
    query = request.POST.get('query')


    try:
        client = wolframalpha.Client("")
        res = client.query(query)
        ans = next(res.results).text
        return render(request, 'chatbot.html', {'ans': ans, 'query': query})


    except Exception:
        try:
            ans = wikipedia.summary(query, sentences=10)
            return render(request, 'chatbot.html', {'ans': ans, 'query': query})


        except Exception:
            ans = "FOUND NOTHING"
            return render(request, 'chatbot.html', {'ans': ans, 'query': query})
