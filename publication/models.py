from django.db import models
from taggit.managers import TaggableManager
from django.utils import timezone


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')


class Publication(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Brouillon'),
    ('published', 'Publié'),
    )
    title = models.CharField(max_length=255, verbose_name = "Titre")
    slug = models.SlugField(verbose_name = "url")
    intro = models.TextField(verbose_name = "Texte d'introduction")
    document = models.FileField(upload_to='media/', null=True)
    body = models.TextField(verbose_name = "Contenu")
    publish = models.DateTimeField(default=timezone.now, verbose_name = "Date de publication")
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name = "Date d'ajout")

    class Meta:
        ordering = ['-date_added']
    
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    tags = TaggableManager()

