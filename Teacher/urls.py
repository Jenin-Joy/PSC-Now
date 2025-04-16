from django.urls import path,include
from Teacher import views
from User.models import *

app_name="Teacher"
urlpatterns = [
   
     path('profile',views.profile,name='profile'),
     path('home/',views.home,name='homepage'),
     path('EditProfile/',views.EditProfile,name='EditProfile'),
     path('ChangePassword/',views.ChangePassword,name='ChangePassword'),
     path('Viewuser/',views.Viewuser,name="Viewuser"),
     path('Addstudymaterials/',views.Addstudymaterials,name="Addstudymaterials"),
     path('smdelete/<int:id>',views.smdelete,name='smdelete'),
     path('delteacher/<int:id>',views.delteacher,name='delteacher'),
     path('complaint/',views.complaint,name="complaint"),
     path('classes/',views.classes,name="classes"),
    #  path('questions/',views.questions,name="questions"),
      path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    
    path('clearchat/',views.clearchat,name="clearchat"),
    path('examinationdetails/',views.examinationdetails,name='examinationdetails'),
    path('startexam/<int:id>',views.startexam,name='startexam'),
    path('delexm/<int:id>',views.delexm,name='delexm'),
    path('addquestions/<int:id>',views.addquestions,name='addquestions'),
    path('delqus/<int:id>/<int:did>',views.delqus,name='delqus'),
    path('addoptions/<int:id>',views.addoptions,name='addoptions'),
    path('delopt/<int:id>/<int:did>',views.delopt,name='delopt'),
    path('completedexam/',views.completedexam,name='completedexam'),
    path('viewresult/<int:id>',views.viewresult,name='viewresult'),
    path('completeexam/<int:id>',views.completeexam,name='completeexam'),
    path('viewranklist/<int:id>',views.viewranklist,name='viewranklist'),
    path('startclass/<int:status>',views.startclass,name='startclass'),
]