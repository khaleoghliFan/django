from django.urls import path
from . import views  # ایمپورت ویوها

urlpatterns = [
    path('', views.todo_list, name='todo_list'),  # نمایش لیست وظایف
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),  # حذف وظیفه
    path('complete/<int:task_id>/', views.task_complete, name='task_complete'),  # تکمیل وظیفه
]
