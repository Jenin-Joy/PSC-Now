from django.urls import path,include
from User import views

app_name="User"
urlpatterns = [
    path('home/',views.home,name='home'),
    path('MyProfile/',views.MyProfile,name='MyProfile'),
    # # path('editprofile',views.editprofile,name='editprofile'),
    path('EditProfile/',views.EditProfile,name='EditProfile'),
    path('ChangePassword/',views.ChangePassword,name='ChangePassword'),
    path('Viewteacher/',views.Viewteacher,name="Viewteacher"),
    path('deluser/<int:id>',views.deluser,name='deluser'),
    path('complaint/',views.complaint,name="complaint"),
    path('Viewclass/<int:id>',views.Viewclass,name="Viewclass"),
    path('feedbacks/',views.feedbacks,name="feedbacks"),
    path('deletefeedback/<int:id>',views.deletefeedback,name='deletefeedback'),
    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),
    path('viewexam/',views.viewexam,name='viewexam'),
    path('viewquestion/<int:id>',views.viewquestion,name='viewquestion'),
    path('ajaxexamanswer/',views.ajaxexamanswer,name='ajaxexamanswer'),
    path('ajaxtimer/',views.ajaxtimer,name='ajaxtimer'),
    path('successer/',views.successer,name='successer'),

    path('viewresult/<int:id>',views.viewresult,name='viewresult'),
    path('rating/<int:mid>',views.rating,name="rating"),  
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
    path('starrating/',views.starrating,name="starrating"),
     path('logout/',views.logout,name='logout'),
]