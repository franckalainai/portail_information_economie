from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('bios/', views.biographie, name="bios"),
    path('flashs/', views.flash, name="flashs"),
    path('communiques/', views.communique, name="communiques"),
    path('agendas/', views.agenda, name="agendas"),
    path('actualites/', views.actualite, name="actualites"),
    path('publications/', views.publication, name="publications"),
    path('<slug:post>/', views.post_detail, name='post_detail'),
    path('bio/<str:slug>/', views.bio_detail, name='bio_detail'),
    path('flash/<str:slug>/', views.flash_detail, name='flash_detail'),
    path('communique/<str:slug>/', views.communique_detail, name='communique_detail'),
    path('agenda/<str:slug>/', views.agenda_detail, name='agenda_detail'),
    path('actualite/<str:slug>/', views.actualite_detail, name='actualite_detail'),
    path('publication/<str:slug>/', views.publication_detail, name='publication_detail'),
]
