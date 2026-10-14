from django.urls import path

from . import views

app_name = 'todolist'

urlpatterns = [
    path('', views.task_list, name='index'),
    path('add/', views.add_task, name='add_task'),
    path('<int:task_id>/delete/', views.delete_task, name='delete'),
    path('<int:task_id>/toggle/', views.toggle_task, name='update'),
]
