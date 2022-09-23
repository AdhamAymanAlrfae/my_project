from django.urls import path 
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('long_in', Log_in.as_view(), name='login'),
    path('long_out', LogoutView.as_view(next_page='login'), name='logout'),
    path('', Home.as_view(), name='home'),
    path('task/<int:pk>/',Show_Task.as_view(), name='task' ),
    path('create/',Create_Task.as_view(),name='create'),
    path('update/<int:pk>/', Update_Task.as_view(), name='update'),
    path('delete/<int:pk>/',Delete_Task.as_view(), name='delete'),
    path('register/',Register_Page.as_view(), name='register')

]