from django.db import models
from taggit.managers import TaggableManager
from django.utils import timezone
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Brouillon'),
    ('published', 'Publié'),
    )
    title = models.CharField(max_length=255, verbose_name = "Titre")
    slug = models.SlugField(verbose_name = "url")
    intro = models.TextField(verbose_name = "Texte d'introduction")
    image = models.ImageField(upload_to ='media/', null=True)
    body = models.TextField(verbose_name = "Contenu")
    publish = models.DateTimeField(default=timezone.now, verbose_name = "Date de publication")
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name = "Date d'ajout")

    class Meta:
        ordering = ['-date_added']
        verbose_name = "Article"

    
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    tags = TaggableManager()


class Bio(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Brouillon'),
    ('published', 'Publié'),
    )
    title = models.CharField(max_length=255, verbose_name = "Titre")
    slug = models.SlugField(verbose_name = "url")
    intro = models.TextField(verbose_name = "Texte d'introduction")
    image = models.ImageField(upload_to ='media/', null=True)
    body = models.TextField(verbose_name = "Contenu")
    publish = models.DateTimeField(default=timezone.now, verbose_name = "Date de publication")
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name = "Date d'ajout")

    class Meta:
        ordering = ['-date_added']
        verbose_name = 'Biographie'

        
    
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    tags = TaggableManager()

    def get_absolute_url(self): #url name
       # return reverse('article-detail', args=(str(self.id)))
       return reverse('bio_detail')

    

class Flash(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Brouillon'),
    ('published', 'Publié'),
    )
    title = models.CharField(max_length=255, verbose_name = "Titre")
    slug = models.SlugField(verbose_name = "url")
    intro = models.TextField(verbose_name = "Texte d'introduction")
    image = models.ImageField(upload_to ='media/', null=True)
    body = models.TextField(verbose_name = "Contenu")
    publish = models.DateTimeField(default=timezone.now, verbose_name = "Date de publication")
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name = "Date d'ajout")

    class Meta:
        ordering = ['-date_added']
        verbose_name = 'Flash economique'
    
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    tags = TaggableManager()

    def get_absolute_url(self): #url name
       # return reverse('article-detail', args=(str(self.id)))
       return reverse('flash_detail')
    

class Communique(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Brouillon'),
    ('published', 'Publié'),
    )
    title = models.CharField(max_length=255, verbose_name = "Titre")
    slug = models.SlugField(verbose_name = "url")
    intro = models.TextField(verbose_name = "Texte d'introduction")
    image = models.ImageField(upload_to ='media/', null=True)
    body = models.TextField(verbose_name = "Contenu")
    publish = models.DateTimeField(default=timezone.now, verbose_name = "Date de publication")
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name = "Date d'ajout")

    class Meta:
        ordering = ['-date_added']
        verbose_name = 'Communique'
    
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    tags = TaggableManager()

    def get_absolute_url(self): #url name
       # return reverse('article-detail', args=(str(self.id)))
       return reverse('communique_detail')
    
class Agenda(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Brouillon'),
    ('published', 'Publié'),
    )
    title = models.CharField(max_length=255, verbose_name = "Titre")
    slug = models.SlugField(verbose_name = "url")
    intro = models.TextField(verbose_name = "Texte d'introduction")
    image = models.ImageField(upload_to ='media/', null=True)
    body = models.TextField(verbose_name = "Contenu")
    publish = models.DateTimeField(default=timezone.now, verbose_name = "Date de publication")
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name = "Date d'ajout")

    class Meta:
        ordering = ['-date_added']
        verbose_name = 'Agenda'
    
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    tags = TaggableManager()

    def get_absolute_url(self): #url name
       # return reverse('article-detail', args=(str(self.id)))
       return reverse('agenda_detail')
    
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
        verbose_name = 'Publication'
    
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    tags = TaggableManager()

    def get_absolute_url(self): #url name
       # return reverse('article-detail', args=(str(self.id)))
       return reverse('publication_detail')
    

class Actualite(models.Model):
    STATUS_CHOICES = (
    ('draft', 'Brouillon'),
    ('published', 'Publié'),
    )
    title = models.CharField(max_length=255, verbose_name = "Titre")
    slug = models.SlugField(verbose_name = "url")
    intro = models.TextField(verbose_name = "Texte d'introduction")
    image = models.ImageField(upload_to ='media/', null=True)
    body = models.TextField(verbose_name = "Contenu")
    publish = models.DateTimeField(default=timezone.now, verbose_name = "Date de publication")
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name = "Date d'ajout")

    class Meta:
        ordering = ['-date_added']
        verbose_name = 'Actualite'
    
    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    tags = TaggableManager()

    def get_absolute_url(self): #url name
       # return reverse('article-detail', args=(str(self.id)))
       return reverse('actualite_detail')