"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from todo import views as todo_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todo_views.index, name='index'),
    path('ja/', todo_views.index_ja, name='index_ja'),
    path('<int:task_id>/', todo_views.detail, name='detail'),
    path('ja/<int:task_id>/', todo_views.detail_ja, name='detail_ja'),
    path('<int:task_id>/delete', todo_views.delete, name='delete'),
    path('ja/<int:task_id>/delete', todo_views.delete_ja, name='delete_ja'),
    path('<int:task_id>/update', todo_views.update, name='update'),
    path('ja/<int:task_id>/update', todo_views.update_ja, name='update_ja'),
    path('<int:task_id>/close', todo_views.close, name='close'),
    path('ja/<int:task_id>/close', todo_views.close_ja, name='close_ja'),
    path('search/', todo_views.Search.as_view(), name='search'),
]
