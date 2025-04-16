from django.db import models

# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)
class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)
class tbl_adminreg(models.Model):
    adminreg_name=models.CharField(max_length=50)  
    adminreg_email=models.CharField(max_length=50)
    adminreg_password=models.CharField(max_length=50)    
class tbl_brand(models.Model):
    brand_name=models.CharField(max_length=50)  
class tbl_place(models.Model):
    place_name=models.CharField(max_length=30)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)    
class tbl_subcategory(models.Model):
    subcategory_name=models.CharField(max_length=30)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)

class tbl_subject(models.Model):
    subject_id=models.CharField(max_length=50)
    subject_name=models.CharField(max_length=50)             
class tbl_teacher(models.Model):
    teacher_name=models.CharField(max_length=50)
    teacher_email=models.CharField(max_length=50)
    teacher_contact=models.CharField(max_length=50)
    teacher_address=models.CharField(max_length=50)
    teacher_password=models.CharField(max_length=50)
    teacher_photo=models.FileField(upload_to='assets/teacher/photo')
    subject=models.ForeignKey(tbl_subject,on_delete=models.CASCADE)
    teacher_url = models.CharField(max_length=150)
    teacher_class_status = models.IntegerField(default=0)

        