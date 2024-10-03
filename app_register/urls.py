# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('verfiy/', views.student_login_view, name='login'),
    path('reset-password/',views.register,name='register'),
    path('',views.login_view,name='login_view'),
    path('home/',views.home,name="home")
]
