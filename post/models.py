from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Başlık')
    content = models.TextField(verbose_name='İçerik')
    photo = models.ImageField(null=True, blank=True, verbose_name='Fotoğraf')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, editable=False, max_length=130)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'slug': self.slug})

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']


class Contact(models.Model):
    title = models.CharField(max_length=250, verbose_name='Başlık')
    content = models.CharField(max_length=350, verbose_name='İcerik')
    button_name = models.CharField(max_length=25, verbose_name='Butona ad verin')

    def __str__(self):
        return self.title
