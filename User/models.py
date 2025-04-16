from django.db import models
from User.models import *
from Guest.models import *
from Teacher.models import *
# Create your models here.
class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=50)
    complaint_content=models.CharField(max_length=50)
    complaint_reply=models.CharField(max_length=50)
    complaint_status=models.IntegerField(default=0)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
    teacher=models.ForeignKey(tbl_teacher,on_delete=models.CASCADE,null=True)

class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=200)  

# class tbl_answerhead(models.Model):
#     user=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
#     questionbody=models.ForeignKey(tbl_questionbody,on_delete=models.CASCADE,null=True) 

# class tbl_answerbody(models.Model):
#    answerbody_status=models.CharField(max_length=50)
#    questionbody=models.ForeignKey(tbl_questionbody,on_delete=models.CASCADE,null=True)
#    option=models.ForeignKey(tbl_option,on_delete=models.CASCADE,null=True)


class tbl_chat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    user_from = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_from",null=True)
    user_to = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_to",null=True)
    teacher_from = models.ForeignKey(tbl_teacher,on_delete=models.CASCADE,related_name="teacher_from",null=True)
    teacher_to = models.ForeignKey(tbl_teacher,on_delete=models.CASCADE,related_name="teacher_to",null=True)

class tbl_examinationbody(models.Model):
    examination = models.ForeignKey(tbl_examination, on_delete=models.CASCADE)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
    total_marks = models.IntegerField(default=0)
    examinationbody_status = models.IntegerField(default=0)

class tbl_examinationanswers(models.Model):
    examinationbody = models.ForeignKey(tbl_examinationbody, on_delete=models.CASCADE)
    question = models.ForeignKey(tbl_questions, on_delete=models.CASCADE)
    myanswer = models.ForeignKey(tbl_options, on_delete=models.CASCADE, related_name="myanswer", null=True)
    correct_answer = models.ForeignKey(tbl_options, on_delete=models.CASCADE,related_name="correct_answer")
    examinationanswers_statusq = models.IntegerField(default=0)

class tbl_timmer(models.Model):
    timmer = models.TimeField()
    exam = models.ForeignKey(tbl_examination, on_delete=models.CASCADE)
    timmer_status = models.IntegerField(default=0)

class tbl_rating(models.Model):
     rating_data=models.IntegerField()
     user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
     user_review=models.CharField(max_length=500)
     teacher=models.ForeignKey(tbl_teacher,on_delete=models.CASCADE)
     datetime=models.DateTimeField(auto_now_add=True)