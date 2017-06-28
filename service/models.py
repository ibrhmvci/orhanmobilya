from django.db import models


class ServiceDynamic(models.Model):
    header = models.CharField(max_length=250, verbose_name='Servis Adı')
    content = models.TextField(verbose_name='Servis İçeriği')

    def __str__(self):
        return self.header


class ServiceStatic(models.Model):
    service_title = models.CharField(max_length=250, verbose_name='Servis Başlığı')
    image = models.ImageField(verbose_name='Ana Resim (500x600)')
