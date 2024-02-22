from django.urls import path
from . import views

urlpatterns = [
    path('publications/', views.publications, name="publication"),
    path('<str:slug>/', views.publication_detail, name='publication_detail'),
]
