from django.urls import path
from . import views

urlpatterns = [
    path('actualites/', views.actualites, name="actualite"),
    path('<str:slug>/', views.actualite_detail, name='actualite_detail'),
]
