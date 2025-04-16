from django.shortcuts import render,redirect
from User.models import *
from Guest.models import *
from Admin.models import *
from datetime import datetime
from django.db.models import Q
from django.http import JsonResponse
import json
from datetime import time, datetime, timedelta

def home(request):
        return render(request,'User/Homepage.html',{'home':home})

def MyProfile(request):
        user=tbl_user.objects.get(id=request.session["uid"])
        return render(request,'User/Myprofile.html',{'user':user})

def EditProfile(request):
     b=tbl_user.objects.get(id=request.session["uid"])
     if request.method=="POST":
        b.user_name=request.POST.get("name")
        b.user_email=request.POST.get("email")
        b.user_contact=request.POST.get("contact")
        b.user_address=request.POST.get("address")
        b.save()
        return redirect("User:MyProfile")
     else:
         return render(request,"User/EditProfile.html",{'user':b})

def ChangePassword(request):
     error1="Your Password does'nt match"
     error2="Your old password  does'nt match"
     b=tbl_user.objects.get(id=request.session["uid"])
     olda=b.user_password
     oldb= new=request.POST.get("txt_oldpassword")
     new=request.POST.get("txt_newpassword")
     re=request.POST.get("txt_retypepassword")
     if request.method=="POST":
        if(olda==oldb):
            if(new==re):
                b.user_password=request.POST.get("txt_retypepassword")
                b.save()
                return redirect("User:MyProfile")
            else:
                return render(request,"User/ChangePassword.html")
        else:
            return render(request,"User/ChangePassword.html")
     else:
         return render(request,"User/ChangePassword.html")
def Viewteacher(request):
    ar=[1,2,3,4,5]
    parry=[]
    avg=0
    tea=tbl_teacher.objects.all()
    for i in tea:
        tot=0
        ratecount=tbl_rating.objects.filter(teacher=i.id).count()
        if ratecount>0:
            ratedata=tbl_rating.objects.filter(teacher=i.id)
            for j in ratedata:
                tot=tot+j.rating_data
                avg=tot//ratecount
                #print(avg)
            parry.append(avg)
        else:
            parry.append(0)
        # print(parry)
    datas=zip(tea,parry)
    return render(request,'User/Viewteacher.html',{'teacher':datas,'ar':ar})
def Viewclass(request, id):
    classes=tbl_classvideo.objects.filter(teacher=id)
    return render(request,'User/Viewclass.html',{'classes':classes})
def complaint(request):
    user=tbl_user.objects.all()
    complaint=tbl_complaint.objects.filter(user__in=user)
    user=tbl_user.objects.get(id=request.session['uid'])
    if request.method == "POST":
        print(request.POST.get('text_content'))
        title=request.POST.get('txt_title')
        content=request.POST.get('text_content')
        btn=request.POST.get('btnsubmit')
        tbl_complaint.objects.create(complaint_title=title,complaint_content=content,user=user)
        return redirect("User:complaint")
    else:
       return render(request,"User/Complaint.html",{'result':complaint})    
def deluser(request,id):
    tbl_complaint.objects.get(id=id).delete()
    return redirect("User:complaint")
def feedbacks(request):
    feedback=tbl_feedback.objects.all()
    if request.method == "POST":
        content=request.POST.get('text_content')
        tbl_feedback.objects.create(feedback_content=content)
        return render(request,"User/Feedbacks.html",{'result':feedback})
    else:
        return render(request,"User/Feedbacks.html",{'result':feedback})
def deletefeedback(request,id):
      tbl_feedback.objects.get(id=id).delete()
      return redirect("User:feedbacks")
def chatpage(request,id):
    user  = tbl_teacher.objects.get(id=id)
    return render(request,"User/Chat.html",{"user":user})

def ajaxchat(request):
    from_user = tbl_user.objects.get(id=request.session["uid"])
    to_teacher = tbl_teacher.objects.get(id=request.POST.get("tid"))
    print(to_teacher)
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,teacher_to=to_teacher,chat_file=request.FILES.get("file"))
    return render(request,"User/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_user.objects.get(id=request.session["uid"])
    chat_data = tbl_chat.objects.filter((Q(user_from=user) | Q(user_to=user)) & (Q(teacher_from=tid) | Q(teacher_to=tid))).order_by('chat_time')
    return render(request,"User/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(user_from=request.session["uid"]) & Q(teacher_to=request.GET.get("tid")) | (Q(teacher_from=request.GET.get("tid")) & Q(user_to=request.session["uid"]))).delete()
    return render(request,"User/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."}) 

def viewexam(request):
    exam = tbl_examination.objects.all()
    for i in exam:
        exambodycount = tbl_examinationbody.objects.filter(examination=i.id,user=request.session["uid"],examinationbody_status=1).count()
        if exambodycount > 0:
            i.examstatus = 1
    return render(request,"User/ViewExam.html",{'exam':exam})

def viewquestion(request,id):
    question = tbl_questions.objects.filter(examination=id)
    optioncount = 0
    for i in question:
        count = tbl_options.objects.filter(questions=i.id).count()
        if count > 0:
            optioncount = optioncount + 1
    examcount = tbl_examinationbody.objects.filter(examination=id,user=request.session["uid"]).count()
    if examcount > 0:
        exambodyid = tbl_examinationbody.objects.get(examination=id,user=request.session["uid"])
        return render(request,"User/ViewQuestion.html",{'questions':question,"exambodyid":exambodyid.id,"optioncount":optioncount,"examination_id":id})
    else:
        exambodyid = tbl_examinationbody.objects.create(user=tbl_user.objects.get(id=request.session["uid"]),examination=tbl_examination.objects.get(id=id))
        return render(request,"User/ViewQuestion.html",{'questions':question,"exambodyid":exambodyid.id,"optioncount":optioncount,"examination_id":id})

def ajaxexamanswer(request):
    exam_answer = request.GET.get('answers')
    answers_dict = json.loads(exam_answer)
    for question_key, option_id in answers_dict.items():
        questionid = question_key.split("_")[1]
        options = tbl_options.objects.get(questions=questionid,status=True)
        if option_id == None:
            tbl_examinationanswers.objects.create(examinationbody=tbl_examinationbody.objects.get(id=request.GET.get('exambodyid')),question=tbl_questions.objects.get(id=questionid),correct_answer=tbl_options.objects.get(id=options.id))
        else:
            tbl_examinationanswers.objects.create(examinationbody=tbl_examinationbody.objects.get(id=request.GET.get('exambodyid')),question=tbl_questions.objects.get(id=questionid),myanswer=tbl_options.objects.get(id=option_id),correct_answer=tbl_options.objects.get(id=options.id))
    exambody = tbl_examinationbody.objects.get(id=request.GET.get('exambodyid'))
    exambody.examinationbody_status = 1
    exambody.save()
    return JsonResponse({"msg":"Examination Submitted Sucessfully..."})

def ajaxtimer(request):
    exam = tbl_examination.objects.get(id=request.GET.get('exam'))
    timecount = tbl_timmer.objects.filter(exam=exam).count()
    if timecount > 0:
        timer_obj = tbl_timmer.objects.get(exam=exam)
        if timer_obj.timmer > time(0, 0, 0):
            current_datetime = datetime.combine(datetime.today(), timer_obj.timmer)
            new_datetime = current_datetime - timedelta(seconds=1)
            new_time = new_datetime.time()
            timer_obj.timmer = new_time
            timer_obj.save()
            time_str = new_time.strftime("%H:%M:%S")
            return JsonResponse({"msg": time_str,"status":False})
        else:
            exam.examination_status = 2
            exam.save()
            return JsonResponse({"msg": "Time's up","status":True})
    else:
        tbl_timmer.objects.create(exam=exam,timmer=exam.time)
        return JsonResponse({"msg": ""})

def successer(request):
    return render(request,"User/Success.html")

def viewresult(request, id):
    resultcount = tbl_examinationanswers.objects.filter(examinationbody__examination=id,examinationbody__user=request.session["uid"],examinationbody__examinationbody_status=1).count()
    if resultcount == 0:
        return render(request,"User/viewResult.html",{"msg":"Result Not Found"})
    result = tbl_examinationanswers.objects.filter(examinationbody__examination=id,examinationbody__user=request.session["uid"],examinationbody__examinationbody_status=1)
    question = tbl_questions.objects.filter(examination=id).count()
    if result[0].examinationbody.total_marks == 0:
        total = 0
        for i in result:
            if i.myanswer and i.myanswer.id == i.correct_answer.id:
                total += 1
        exambody = tbl_examinationbody.objects.get(examination=id,user=request.session["uid"],examinationbody_status=1)
        exambody.total_marks = total
        exambody.save()
    return render(request,"User/viewResult.html",{"result": result,"question":question})  
def rating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    # wdata=tbl_booking.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(teacher=mid).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(teacher=mid).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        # print(avg)
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    user_review=request.GET.get('user_review')
    tid=request.GET.get('tid')
    # wdata=tbl_booking.objects.get(id=pid)
    tbl_rating.objects.create(user=tbl_user.objects.get(id=request.session["uid"]),user_review=user_review,rating_data=rating_data,teacher=tbl_teacher.objects.get(id=tid))
    stardata=tbl_rating.objects.filter(teacher=tid).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    # cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
    rate = tbl_rating.objects.filter(teacher=request.GET.get("pdt"))
    ratecount = tbl_rating.objects.filter(teacher=request.GET.get("pdt")).count()
    for i in rate:
        if int(i.rating_data) == 5:
            five = five + 1
        elif int(i.rating_data) == 4:
            four = four + 1
        elif int(i.rating_data) == 3:
            three = three + 1
        elif int(i.rating_data) == 2:
            two = two + 1
        elif int(i.rating_data) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        # print(i.rating_data)
        # r_len = r_len + int(i.rating_data)
    # rlen = r_len // 5
    # print(rlen)
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
    return JsonResponse(result) 
def logout(request):
    del request.session["uid"]
    return redirect("Guest:login")


# Create your views here.