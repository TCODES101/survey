from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('collect', views.collect, name='collect'),
    path('signup', views.signup, name='signup'),
    path('loginf', views.loginf, name='loginf'),
    path('loginProcess', views.loginProcess, name='loginProcess'),
    path('signupProcess', views.signupProcess, name='signupProcess'),
    path('admin2',views.admin2, name='admin2'),
    path('intake',views.intake, name='intake'),
    path('staff',views.staff, name='staff'),
    path('graduates',views.graduates, name='graduates'),
    path('graduatesPdf',views.graduatesPdf, name='graduatesPdf'),
    path('intakePdf',views.intakePdf, name='intakePdf'),
    path('staffPdf',views.staffPdf, name='staffPdf'),
    path('ssPdf',views.ssPdf, name='ssPdf'),
    path('cPdf',views.cPdf, name='cPdf'),
    path('skill',views.skill, name='skill'),
    path('challenge',views.challenge, name='challenge'),
    path('logoutUser',views.logoutUser, name='logoutUser'),

    #password reset
    path('reset_password/', 
    auth_views.PasswordResetView.as_view(template_name="myapp/templates/reset_password.html"),
    name='reset_password'),

    path('reset_password_sent/', 
    auth_views.PasswordResetDoneView.as_view(template_name="myapp/templates/password_sent.html"),
    name='password_reset_done'),

    path('reset/<uidb64>/<token>/', 
    auth_views.PasswordResetConfirmView.as_view(template_name="myapp/templates/password_complete.html"),
    name='password_reset_confirm'),

    path('reset_password_complete', 
    auth_views.PasswordResetCompleteView.as_view(template_name="myapp/templates/reset_done.html"), 
    name='password_reset_complete'),
    

]