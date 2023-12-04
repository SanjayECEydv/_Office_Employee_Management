
from turtle import home
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("home/", employee_home),
    path('add-employee/', add_employee),
    path('delete-emp/<int:emp_id>', delete_emp),
    path('update-emp/<int:emp_id>', update_emp),
    path('do-update-emp/<int:emp_id>', do_update_emp),
    
]
