
from django.contrib import admin
from django.urls import include, path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='home'),
    path('add/', views.add_task, name='add_task'),
    path('complete/<int:task_id>/', views.complete_task, name='complete_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('update/<int:task_id>/', views.update_task, name='update_task'),
    path('index/', views.index, name='index'),
]
