from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('planner/detail/<int:planner_id>',views.detail_planner, name = 'detail_planner'),
    path('planner/create/',views.create_planner, name = 'create_planner'),
    path('planner/update/<int:planner_id>',views.update_planner, name = 'update_planner'),
]   
