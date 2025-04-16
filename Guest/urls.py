from django.urls import path,include
from Guest import views
app_name="Guest"
urlpatterns = [
    path('login/',views.login,name='login'),
    path('Registration/',views.Registration,name='Registration'),
    path('Ajaxplace/',views.Ajaxplace,name='Ajaxplace'),
    path('',views.index,name='index'),

    path('payment/<int:id>/',views.payment,name="payment"),
    path('loader/',views.loader, name='loader'),
    path('paymentsuc/',views.paymentsuc, name='paymentsuc'),
]