from django.db import models


class MainGallery(models.Model):
    title = models.CharField(max_length=30, verbose_name='Başlık')
    content = models.TextField(verbose_name='İçerik Bilgisi')
    image = models.ImageField(verbose_name='Galerinin Ana Resmi')
    link = models.URLField(verbose_name='Link')

    def __str__(self):
        return self.title