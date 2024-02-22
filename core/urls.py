from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<slug:post>/', views.post_detail, name='post_detail'),
]
