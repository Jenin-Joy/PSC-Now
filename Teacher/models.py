from django.db import models
from Admin.models import *

class tbl_studymaterials(models.Model):
    studymaterials_name=models.CharField(max_length=50)
    studymaterials_details=models.CharField(max_length=50)
    studymaterials_file=models.FileField(upload_to='assets/teacher/photo')
    subject=models.ForeignKey(tbl_subject,on_delete=models.CASCADE)
    teacher=models.ForeignKey(tbl_teacher,on_delete=models.CASCADE)

class tbl_classvideo(models.Model):
    class_title=models.CharField(max_length=50)
    class_desc=models.CharField(max_length=50)
    class_file=models.FileField(upload_to='assets/teacher/photo')
    teacher=models.ForeignKey(tbl_teacher,on_delete=models.CASCADE)

class tbl_examination(models.Model):
    examination_name=models.CharField(max_length=50) 
    examination_mark=models.CharField(max_length=50) 
    examination_qno=models.CharField(max_length=50) 
    examination_time=models.CharField(max_length=50) 
    examination_status = models.IntegerField(default=0)
    time = models.TimeField(null=True)
    start_time = models.TimeField(null=True)
    teacher=models.ForeignKey(tbl_teacher,on_delete=models.CASCADE,null=True)

class tbl_questions(models.Model):
    question=models.CharField(max_length=100) 
    examination=models.ForeignKey(tbl_examination,on_delete=models.CASCADE)

class tbl_options(models.Model):
    questions=models.ForeignKey(tbl_questions,on_delete=models.CASCADE)
    answer=models.CharField(max_length=100)
    status = models.BooleanField() 

        
    
