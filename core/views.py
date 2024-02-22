from django.shortcuts import get_object_or_404, render, redirect
from django.db.models import Count

#from publication.models import *

from .models import *
from actualite.models import *

def index(request):
    posts = Post.objects.all()
    actualites = Actualite.objects.all()
    #publications = Publication.objects.all()
    return render(request, 'home.html', {'posts': posts, 'actualites': actualites})

def post_detail(request, post):
    #post = Post.objects.get(slug=slug)
    post=get_object_or_404(Post,slug=post,status='published')
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags','-publish')[:6]

    return render(request, 'detail.html', {'post': post, 'similar_posts':similar_posts,})
