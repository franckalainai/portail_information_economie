# Generated by Django 3.2.24 on 2024-02-22 11:38

from django.db import migrations, models
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Titre')),
                ('slug', models.SlugField(verbose_name='url')),
                ('intro', models.TextField(verbose_name="Texte d'introduction")),
                ('image', models.ImageField(null=True, upload_to='media/')),
                ('body', models.TextField(verbose_name='Contenu')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date de publication')),
                ('status', models.CharField(choices=[('draft', 'Brouillon'), ('published', 'Publié')], default='draft', max_length=10)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name="Date d'ajout")),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]
