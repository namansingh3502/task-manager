from django.urls import path, include
from . import views

urlpatterns = [

    path('task-list/', views.task_list, name="task-list"),
    path('task-detail/<str:task_id>/', views.task_detail, name="task-detail"),
    path('task-create/', views.task_create, name="task-create"),

    path('task-update/<str:task_id>/', views.task_update, name="task-update"),
    path('task-delete/<str:task_id>/', views.task_delete, name="task-delete"),
]
