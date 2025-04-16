from django.shortcuts import render,redirect

from Guest.models import *
from Admin.models import *
from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta
# Create your views here.

def index(request):
    expired = tbl_payment.objects.filter(payment_enddate=date.today(),payment_status=0)
    for i in expired:
        i.payment_status = 1
        i.save()
        user = tbl_user.objects.get(id=i.user.id)
        user.user_status = 0
        user.save()
    return render(request,'Guest/index.html')

def Registration(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        address=request.POST.get("address")
        contact=request.POST.get("contact")
        password=request.POST.get("password")
       
        place=tbl_place.objects.get(id=request.POST.get("place"))
        photo=request.FILES.get("file_photo")
        user = tbl_user.objects.create(user_name=name,user_email=email,user_address=address,user_contact=contact,user_password=password,place=place,user_photo=photo)
        return redirect("Guest:payment",user.id)
    return render(request,'Guest/Registration.html',{'result':dis})
    #else:
    #   return render(request,'Guest/Registration.html')
    
def Ajaxplace(request):
    place=tbl_place.objects.filter(district=request.GET.get("did"))
    return render(request,'Guest/Ajaxplace.html',{'place':place})

def login(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        admincount=tbl_adminreg.objects.filter(adminreg_email=email,adminreg_password=password).count()
        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        teachercount=tbl_teacher.objects.filter(teacher_email=email,teacher_password=password).count()
        # print(usercount)
        if usercount > 0:
            user=tbl_user.objects.get(user_email=email,user_password=password)
            if user.user_status == 0:
                return redirect("Guest:payment",user.id)
            else:
                request.session["uid"]=user.id
                return redirect("User:home")
        elif teachercount > 0:
            teacher=tbl_teacher.objects.get(teacher_email=email,teacher_password=password)
            request.session["tid"]=teacher.id
            return redirect("Teacher:homepage")

        elif admincount > 0:
            admin=tbl_adminreg.objects.get(adminreg_email=email,adminreg_password=password)
            request.session["aid"]=admin.id
            return redirect("Admin:homepage")
    
        else:
            return render(request,'Guest/Login.html')
    else:
        return render(request,'Guest/Login.html')

def payment(request, id):
    if request.method == "POST":
        today = date.today()
        tbl_payment.objects.create(
            user=tbl_user.objects.get(id=id),
            payment_startdate=today,
            payment_enddate=today + relativedelta(months=7)
        )
        user = tbl_user.objects.get(id=id)
        user.user_status = 1
        user.save()
        return redirect("Guest:loader")
    else:
        return render(request,"Guest/Payment.html")

def loader(request):
    return render(request,"Guest/Loader.html")

def paymentsuc(request):
    return render(request, 'Guest/Payment_suc.html')