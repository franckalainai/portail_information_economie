from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Count

from .models import *

def publications(request):
    publications = Publication.objects.all()
    return render(request, 'publications/home.html', {'publications': publications})


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