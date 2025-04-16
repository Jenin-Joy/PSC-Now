from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *
# Create your views here.
def add(request):
    if request.method=="POST":
        a=int(request.POST.get("num1"))
        b=int(request.POST.get("num2"))
        c=a+b
        return render(request,'Admin/Add.html',{'result':c})
    else:
        return render(request,"Admin/Add.html")



def largest(request):
    if request.method=="POST":
        a=int(request.POST.get("num1"))
        b=int(request.POST.get("num2"))
        if(a>b):
            return render(request,'Admin/Largest.html',{'result':a})
        else:
            return render(request,'Admin/Largest.html',{'result':b}) 
    else:
        return render(request,'Admin/Largest.html')

def calculator(request):
    if request.method=="POST":
        a=int(request.POST.get("num1"))
        b=int(request.POST.get("num2"))
        btn=request.POST.get("btn")
        if btn=='+':
            c=a+b
            return render(request,'Admin/Calculator.html',{'result':c})
        elif btn=='-':
            c=a-b
            return render(request,'Admin/Calculator.html',{'result':c})
        elif btn=='*':
            c=a*b
            return render(request,'Admin/Calculator.html',{'result':c})
        elif btn=='/':
            c=a/b
            return render(request,'Admin/Calculator.html',{'result':c})
    else:
        return render(request,'Admin/Calculator.html')

def district(request):
    dis=tbl_district.objects.all()
    if request.method=="POST":
        district=request.POST.get('dis')
        tbl_district.objects.create(district_name=district)
        
        return render(request,'Admin/district.html',{'district':dis})
    else:
        return render(request,'Admin/district.html',{'district':dis})
def category(request):
    cat=tbl_category.objects.all()
    if request.method=="POST":
        category=request.POST.get('cat')
        tbl_category.objects.create(category_name=category)
        return render(request,'Admin/category.html',{'category':cat})
    else:
        return render(request,'Admin/category.html',{'category':cat})
def subcategory(request):
    cat=tbl_category.objects.all()#select
    subcategory=tbl_subcategory.objects.all()
    if request.method=="POST":
        cat=tbl_category.objects.get(id=request.POST.get("seld"))
        tbl_subcategory.objects.create(subcategory_name=request.POST.get("subcategory"),category=cat)
        return redirect("Admin:subcategory")
    else:
        return render(request,'Admin/Subcategory.html',{'category':cat,'sub':subcategory})        
def adminreg(request):
    adm=tbl_adminreg.objects.all()
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        tbl_adminreg.objects.create(adminreg_name=name,adminreg_email=email,adminreg_password=password)
        return render(request,'Admin/AdminReg.html',{'adminreg':adm})
    else:
        return render(request,'Admin/AdminReg.html',{'adminreg':adm})
def adelete(request,id):
    tbl_adminreg.objects.get(id=id).delete()
    return redirect("Admin:AdminReg")
def ddelete(request,id):
    tbl_district.objects.get(id=id).delete()
    return redirect("Admin:district")
def pdelete(request,id):
    tbl_place.objects.get(id=id).delete()
    return redirect("Admin:place")    
def place(request):
    dis=tbl_district.objects.all()#select
    place=tbl_place.objects.all()
    if request.method=="POST":
        dist=tbl_district.objects.get(id=request.POST.get("seld"))
        tbl_place.objects.create(place_name=request.POST.get("place"),district=dist)
        return redirect("Admin:place")
    else:
        return render(request,'Admin/Place.html',{'district':dis,'pla':place})
def brand(request):
    br=tbl_brand.objects.all()
    if request.method=="POST":
        brand=request.POST.get('br')
        tbl_brand.objects.create(brand_name=brand)
        return render(request,'Admin/brand.html',{'brand':br})
    else:
        return render(request,'Admin/brand.html',{'brand':br})  
def bdelete(request,id):
    tbl_brand.objects.get(id=id).delete()
    return redirect("Admin:brand")
def bedit(request,id):
    brand=tbl_brand.objects.get(id=id)
    if request.method=="POST":
        brand.brand_name=request.POST.get("br")
        brand.save()
        return redirect('Admin:brand')
    else:
        return render(request,'Admin/brand.html',{'bran':brand})  
def cdelete(request,id):
    tbl_subcategory.objects.get(id=id).delete()
    return redirect("Admin:subcategory")
def cedit(request,id):
    category=tbl_category.objects.all()
    sanam=tbl_subcategory.objects.get(id=id)
    if request.method=="POST":
        sanam.subcategory_name=request.POST.get("subcategory")
        sanam.save()
        return redirect('Admin:subcategory')
    else:
        return render(request,'Admin/subcategory.html',{'su':sanam,'category':category})


def teacher(request):
    sub=tbl_subject.objects.all()
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        address=request.POST.get("address")
        contact=request.POST.get("contact")
        password=request.POST.get("password")
        proof=request.POST.get("proof")
        photo=request.FILES.get("file_photo")
        subj=tbl_subject.objects.get(id=request.POST.get("Subjectid"))
        tbl_teacher.objects.create(teacher_name=name,teacher_email=email,teacher_address=address,teacher_contact=contact,teacher_password=password,teacher_photo=photo,subject=subj)
        return render(request,'Admin/Teacherregistration.html',{'subject':sub})
    else:
      return render(request,'Admin/Teacherregistration.html',{'subject':sub})                        
def subject(request):
    sub=tbl_subject.objects.all()
    if request.method=="POST":
        subject=request.POST.get('sub')
        tbl_subject.objects.create(subject_name=subject)
        
        return render(request,'Admin/subject.html',{'subject':sub})
    else:
        return render(request,'Admin/subject.html',{'subject':sub})
def sdelete(request,id):
    tbl_subject.objects.get(id=id).delete()
    return redirect("Admin:subject")
def Viewteacher(request):
    tea=tbl_teacher.objects.all()
    if request.method=="POST":
        teacher=request.POST.get('tea')
        tbl_teacher.objects.create(teacher_name=teacher)
        
        return render(request,'Admin/Viewteacher.html',{'teacher':tea})
    else:
        return render(request,'Admin/Viewteacher.html',{'teacher':tea})
def Viewuser(request):
    use=tbl_user.objects.filter(user_status=0)
    accept=tbl_user.objects.filter(user_status=1)
    reject=tbl_user.objects.filter(user_status=2)
    return render(request,'Admin/Viewuser.html',{'result':use,'accept':accept,'reject':reject})

def useraccept(request,id):
    use=tbl_user.objects.get(id=id)
    use.user_status=1
    use.save()
    return redirect("Admin:Viewuser")

def userreject(request,id):
    use=tbl_user.objects.get(id=id)
    use.user_status=2
    use.save()
    return redirect("Admin:Viewuser")

def accepteduser(request):
    use=tbl_user.objects.filter(user_status=1)
    if request.method=="POST":
        return render(request,'Admin/Accepteduser.html',{'result':use})
    else:
        return render(request,'Admin/Accepteuser.html',{'result':use})

def rejecteduser(request):
    use=tbl_user.objects.filter(user_status=2)
    if request.method=="POST":
        return render(request,'Admin/Rejecteduser.html',{'result':use})
    else:
        return render(request,'Admin/Rejecteduser.html',{'result':use})
# def teacheraccept(request,id):
#     tea=tbl_teacher.objects.get(id=id)
#     tea.teacher_status=1
#     tea.save()
#     return redirect("Admin:Viewteacher")

def teacherreject(request,id):
    tea=tbl_teacher.objects.get(id=id)
    tea.teacher_status=2
    tea.save()
    return redirect("Admin:Viewteacher")

def acceptedteacher(request):
    tea=tbl_teacher.objects.filter(teacher_status=1)
    if request.method=="POST":
        return render(request,'Admin/Acceptedteacher.html',{'result':tea})
    else:
        return render(request,'Admin/Acceptedteacher.html',{'result':tea})

def rejectedteacher(request):
    tea=tbl_teacher.objects.filter(teacher_status=2)
    if request.method=="POST":
        return render(request,'Admin/Rejectedteacher.html',{'result':tea})
    else:
        return render(request,'Admin/Rejectedteacher.html',{'result':tea})        
def homepage(request): 
    return render(request,'Admin/Homepage.html') 
def replycomplaint(request,id):
    b=tbl_complaint.objects.get(id=id)
    if request.method=="POST":
        b.complaint_reply=request.POST.get("txt_reply")
        b.complaint_status=1
        b.save()
        return redirect("Admin:complaint")
    else:
        return render(request,'Admin/replycomplaint.html')
  
def complaint(request):
    user=tbl_user.objects.all()
    ucomplaint=tbl_complaint.objects.filter(user__in=user)
    teacher=tbl_teacher.objects.all()
    tcomplaint=tbl_complaint.objects.filter(teacher__in=teacher)
    return render(request,'Admin/complaint.html',{'user':ucomplaint,'teacher':tcomplaint})

def Viewfeedbacks(request):
    feedback=tbl_feedback.objects.all()
    return render(request,'Admin/Viewfeedbacks.html',{'result':feedback})