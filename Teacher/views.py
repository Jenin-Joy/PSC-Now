from django.shortcuts import render,redirect
from Admin.models import *
from User.models import *
from Teacher.models import *
from datetime import datetime  
from django.db.models import Q
# Create your views here.
def home(request):
        return render(request,'Teacher/homepage.html')
def profile(request):
        teacher=tbl_teacher.objects.get(id=request.session["tid"])
        return render(request,'Teacher/Myprofile.html',{'Teacher':teacher})
def EditProfile(request):
     b=tbl_teacher.objects.get(id=request.session["tid"])
     if request.method=="POST":
        b.teacher_name=request.POST.get("txt_name")
        b.teacher_email=request.POST.get("txt_email")
        b.teacher_contact=request.POST.get("txt_contact")
        b.teacher_address=request.POST.get("txt_address")
        b.teacher_url=request.POST.get("txt_url")
        b.save()
        return redirect("Teacher:profile")
     else:
         return render(request,"Teacher/EditProfile.html",{'teacher':b})  
def ChangePassword(request):
     error1="Your Password does'nt match"
     error2="Your old password  does'nt match"
     b=tbl_teacher.objects.get(id=request.session["tid"])
     olda=b.teacher_password
     oldb= new=request.POST.get("txt_oldpassword")
     new=request.POST.get("txt_newpassword")
     re=request.POST.get("txt_retypepassword")
     if request.method=="POST":
        if(olda==oldb):
            if(new==re):
                b.teacher_password=request.POST.get("txt_retypepassword")
                b.save()
                return redirect("Teacher:profile")
            else:
                return render(request,"Teacher/ChangePassword.html")
        else:
            return render(request,"Teacher/ChangePassword.html")
     else:
         return render(request,"Teacher/ChangePassword.html")
def Viewuser(request):
    use=tbl_user.objects.all()
    if request.method=="POST":
        user=request.POST.get('use')
        tbl_user.objects.create(user_name=user)
        
        return render(request,'Teacher/Viewuser.html',{'user':use})
    else:
        return render(request,'Teacher/Viewuser.html',{'user':use})    
def Addstudymaterials(request):
    add=tbl_studymaterials.objects.filter(teacher=request.session['tid'])
    if request.method=="POST":
        teach = tbl_teacher.objects.get(id=request.session["tid"])
        name=request.POST.get('name')
        details=request.POST.get('details')
        file=request.FILES.get('file_photo')
        tbl_studymaterials.objects.create(studymaterials_name=name,studymaterials_details=details,studymaterials_file=file,subject=tbl_subject.objects.get(id=teach.subject.id),teacher=tbl_teacher.objects.get(id=request.session["tid"]))
        return render(request,'Teacher/Addstudymaterials.html',{'result':add})    
    else:
        return render(request,'Teacher/Addstudymaterials.html',{'result':add})  
def smdelete(request,id):
    tbl_studymaterials.objects.get(id=id).delete()
    return redirect("Teacher:Addstudymaterials")
def Viewteacher(request):
    tea=tbl_teacher.objects.all()
    if request.method=="POST":
        teacher=request.POST.get('tea')
        tbl_teacher.objects.create(teacher_name=teacher)
        
        return render(request,'User/Viewteacher.html',{'teacher':tea})
    else:
        return render(request,'User/Viewteacher.html',{'teacher':tea})
def Viewclass(request):
    return render(request,'Admin/Viewclass.html',{'Viewclass':Viewclass})
def complaint(request):
    teacher=tbl_teacher.objects.all()
    complaint=tbl_complaint.objects.filter(teacher__in=teacher)
    teacher=tbl_teacher.objects.get(id=request.session['tid'])
    if request.method == "POST":
        print(request.POST.get('text_content'))
        title=request.POST.get('txt_title')
        content=request.POST.get('text_content')
        btn=request.POST.get('btnsubmit')
        tbl_complaint.objects.create(complaint_title=title,complaint_content=content,teacher=teacher)
        return redirect("Teacher:complaint")
    else:
       return render(request,"Teacher/Complaint.html",{'result':complaint})    
def delteacher(request,id):
    tbl_complaint.objects.get(id=id).delete()
    return redirect("Teacher:complaint")                              

def classes(request):
    classes=tbl_classvideo.objects.filter(teacher=request.session['tid'])
    if request.method == "POST":
        tbl_classvideo.objects.create(
            class_title=request.POST.get("txt_title"),
            class_desc=request.POST.get("txt_desc"),
            class_file=request.FILES.get("file_file"),
            teacher=tbl_teacher.objects.get(id=request.session['tid'])
        )
        return redirect("Teacher:classes")
    else:
        return render(request,"Teacher/Class.html",{'classes':classes})
    
# def questions(request):
#     qns=tbl_questionhead.objects.filter(teacher=request.session['tid'])
#     if request.method == "POST":
#         tbl_questionhead.objects.create(
#             qhead_title=request.POST.get("txt_title"),
#             qhead_score=request.POST.get("txt_score"),
#             teacher=tbl_teacher.objects.get(id=request.session['tid'])
#         )
#         return redirect("Teacher:questions")
#     else:
#         return render(request,"Teacher/Questions.html",{'qns':qns})
def chatpage(request,id):
    user  = tbl_user.objects.get(id=id)
    return render(request,"Teacher/Chat.html",{"user":user})

def ajaxchat(request):
    from_teacher = tbl_teacher.objects.get(id=request.session["tid"])
    to_user = tbl_user.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),teacher_from=from_teacher,user_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"Teacher/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_teacher.objects.get(id=request.session["tid"])
    chat_data = tbl_chat.objects.filter((Q(teacher_from=user) | Q(teacher_to=user)) & (Q(user_from=tid) | Q(user_to=tid))).order_by('chat_time')
    return render(request,"Teacher/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(teacher_from=request.session["tid"]) & Q(user_to=request.GET.get("tid")) | (Q(user_from=request.GET.get("tid")) & Q(teacher_to=request.session["tid"]))).delete()
    return render(request,"Teacher/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})  


def examinationdetails(request):
    if "tid" in request.session:
        exm=tbl_examination.objects.filter(teacher=request.session['tid'],examination_status=0)
        teacher=tbl_teacher.objects.get(id=request.session['tid'])
        if  request.method=="POST":
            name=request.POST.get("txt_name")
            qno=request.POST.get("txt_qno")
            ftime = request.POST.get("txt_ftime")
            ttime = request.POST.get("txt_ttime")

            ftime_obj = datetime.strptime(ftime, "%H:%M")
            ttime_obj = datetime.strptime(ttime, "%H:%M")
            time_diff = ttime_obj - ftime_obj
            total_seconds = time_diff.total_seconds()
            hours = int(total_seconds // 3600)
            minutes = int((total_seconds % 3600) // 60)
            
            time = str(hours) +" hours and "+ str(minutes) +" minutes"
            tbl_examination.objects.create(examination_name=name,examination_mark=qno,examination_qno=qno,examination_time=time,teacher=teacher,time=str(time_diff),start_time=ftime)
    
        return render(request,'Teacher/AddExamination.html',{'result':exm})
    else:
        return redirect("Guest:login")    


def startexam(request, id):
    exam = tbl_examination.objects.get(id=id)
    exam.examination_status = 1
    exam.save()
    return redirect("Teacher:examinationdetails")

def viewresult(request, id):
    user = tbl_user.objects.filter(tbl_examinationbody__examination=id)
    return render(request, "Teacher/ViewResult.html", {'user': user})

def addquestions(request,id):
    if "tid" in request.session:

        que=tbl_questions.objects.filter(examination=id)
        if  request.method=="POST":
            examination=tbl_examination.objects.get(id=id)
            questions=request.POST.get("txt_question")
            tbl_questions.objects.create(question=questions,examination=examination)
        return render(request,'Teacher/Addquestion.html',{'result':que,'id':id})
    else:
        return redirect("Guest:login") 
from django.shortcuts import render, redirect
from .models import tbl_questions, tbl_options

def addoptions(request, id):
    que = tbl_options.objects.filter(questions=id)
    if request.method == "POST":
        questions = tbl_questions.objects.get(id=id)
        ans = request.POST.get("txt_answer")
        status = request.POST.get("txt_radio") == "True"
        count = tbl_options.objects.filter(questions=questions, status=True).count()
        if status and count > 0:
            return render(request, 'Teacher/Addoption.html', {
                'msg': "Corrected Answer is already added",
                'result': que,
                'id': id
            })
        else:
            tbl_options.objects.create(
                answer=ans,
                questions=questions,
                status=status
            )
            return redirect("Teacher:addoptions", id=id)
    else:
        return render(request, 'Teacher/Addoption.html', {'result': que, 'id': id})

 

def delexm(request,id): 
    tbl_examination.objects.get(id=id).delete()
    return redirect("Teacher:examinationdetails") 

def delqus(request,id,did): 
    tbl_questions.objects.get(id=id).delete()
    return redirect("Teacher:addquestions",did) 

def delopt(request,id,did): 
    tbl_options.objects.get(id=id).delete()
    return redirect("Teacher:addoptions",did) 


def completedexam(request):
    exm=tbl_examination.objects.filter(teacher=request.session['tid'],examination_status__gt=0)
    return render(request,"Teacher/CompletedExam.html",{"exam":exm})

def completeexam(request,id):
    exam = tbl_examination.objects.get(id=id)
    exam.examination_status = 2
    exam.save()
    tbl_examinationbody.objects.filter(examination=id).update(examinationbody_status=1)
    return redirect("Teacher:completedexam")

def viewranklist(request,id):
    user = tbl_user.objects.filter(tbl_examinationbody__examination=id).order_by('-tbl_examinationbody__total_marks')
    return render(request, "Teacher/ViewRankList.html", {'user': user})

def startclass(request,status):
    teacher = tbl_teacher.objects.get(id=request.session["tid"])
    teacher.teacher_class_status = status
    teacher.save()
    return redirect("Teacher:profile")