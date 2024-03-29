from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Count

#from publication.models import *

from .models import *

def index(request):
    posts = Post.objects.all()
    actualites = Actualite.objects.all()
    agendas = Agenda.objects.all()
    communiques = Communique.objects.all()
    flashs = Flash.objects.all()
    biographies = Bio.objects.all()

    context = {
        'posts': posts, 
        'actualites': actualites,
        'agendas': agendas,
        'communiques': communiques,
        'flashs': flashs,
        'biographies': biographies,
    }
    #publications = Publication.objects.all()
    return render(request, 'home.html', context)

def biographie(request):
    bios = Bio.objects.all()
    #publications = Publication.objects.all()
    return render(request, 'bio/home.html', {'bios': bios,})

def flash(request):
    flashs = Flash.objects.all()
    #publications = Publication.objects.all()
    return render(request, 'flashs/home.html', {'flashs': flashs,})

def communique(request):
    communiques = Communique.objects.all()
    #publications = Publication.objects.all()
    return render(request, 'communiques/home.html', {'communiques': communiques,})

def agenda(request):
    agendas = Agenda.objects.all()
    #publications = Publication.objects.all()
    return render(request, 'agendas/home.html', {'agendas': agendas,})

def actualite(request):
    actualites = Actualite.objects.all()
    #publications = Publication.objects.all()
    return render(request, 'actualites/home.html', {'actualites': actualites,})

def publication(request):
    publications = Publication.objects.all()
    #publications = Publication.objects.all()
    return render(request, 'publications/home.html', {'publications': publications,})

def rubriques_publications(request):
    rubriques = Rubrique.objects.all()
    #publications = Publication.objects.all()
    return render(request, 'publications/rubriques.html', {'rubriques': rubriques,})

def conjonctures(request):
    conjonctures = Conjoncture.objects.all()
    #publications = Publication.objects.all()
    return render(request, 'conjonctures/home.html', {'conjonctures': conjonctures,})

def post_detail(request, post):
    #post = Post.objects.get(slug=slug)
    post=get_object_or_404(Post,slug=post,status='published')
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:6]

    return render(request, 'detail.html', {'post': post, 'similar_posts':similar_posts,})


def bio_detail(request, slug):
    bio=get_object_or_404(Bio,slug=slug,status='published')
    post_tags_ids = bio.tags.values_list('id', flat=True)
    similar_posts = Bio.published.filter(tags__in=post_tags_ids).exclude(id=bio.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:6]
    context = {'similar_posts':similar_posts,}
    try:
        blog_obj = Bio.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'bio/detail.html', context)

def flash_detail(request, slug):
    flash=get_object_or_404(Flash,slug=slug,status='published')
    post_tags_ids = flash.tags.values_list('id', flat=True)
    similar_posts = Flash.published.filter(tags__in=post_tags_ids).exclude(id=flash.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:6]
    context = {'similar_posts':similar_posts,}
    try:
        blog_obj = Flash.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'flashs/detail.html', context)


def communique_detail(request, slug):
    communique=get_object_or_404(Communique,slug=slug,status='published')
    post_tags_ids = communique.tags.values_list('id', flat=True)
    similar_posts = Communique.published.filter(tags__in=post_tags_ids).exclude(id=communique.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:6]
    context = {'similar_posts':similar_posts,}
    try:
        blog_obj = Communique.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'communiques/detail.html', context)

def agenda_detail(request, slug):
    agenda=get_object_or_404(Agenda,slug=slug,status='published')
    post_tags_ids = agenda.tags.values_list('id', flat=True)
    similar_posts = Agenda.published.filter(tags__in=post_tags_ids).exclude(id=agenda.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:6]
    context = {'similar_posts':similar_posts,}
    try:
        blog_obj = Agenda.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'agendas/detail.html', context)

def actualite_detail(request, post):
    actualite=get_object_or_404(Actualite,slug=post,status='published')
    post_tags_ids = actualite.tags.values_list('id', flat=True)
    similar_posts = Actualite.published.filter(tags__in=post_tags_ids).exclude(id=actualite.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:6]
    context = {'similar_posts':similar_posts,}
    try:
        blog_obj = Actualite.objects.filter(slug=post).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'actualites/detail.html', context)

def publication_detail(request, slug):
    publication=get_object_or_404(Publication,slug=slug,status='published')
    post_tags_ids = publication.tags.values_list('id', flat=True)
    similar_posts = Publication.published.filter(tags__in=post_tags_ids).exclude(id=publication.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:6]
    context = {'similar_posts':similar_posts,}
    try:
        blog_obj = Publication.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'publications/detail.html', context)