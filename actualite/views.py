from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Count

from .models import *

def actualites(request):
    actualites = Actualite.objects.all()
    return render(request, 'actualites/home.html', {'actualites': actualites})


def actualite_detail(request, slug):
    actualite=get_object_or_404(Actualite,slug=slug,status='published')
    post_tags_ids = actualite.tags.values_list('id', flat=True)
    similar_posts = Actualite.published.filter(tags__in=post_tags_ids).exclude(id=actualite.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:6]
    context = {'similar_posts':similar_posts,}
    try:
        blog_obj = Actualite.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'actualites/detail.html', context)

