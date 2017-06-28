from django.db import models


class ContactInfo(models.Model):
    address = models.CharField(max_length=255, verbose_name='Adres', null=True, blank=True)
    phone_number = models.CharField(max_length=11, verbose_name='Telefon numarası', null=True, blank=True)
    mobile_number = models.CharField(max_length=11, verbose_name='Mobil Numara', null=True, blank=True)
    email = models.EmailField(verbose_name='E-mail Adresi', null=True, blank=True)


class SocialNetwork(models.Model):
    facebook = models.URLField(verbose_name='Facebook', null=True, blank=True)
    twitter = models.URLField(verbose_name='Twitter', null=True, blank=True)
    instagram = models.URLField(verbose_name='Instagram', null=True, blank=True)
    google_plus = models.URLField(verbose_name='Google Plus', null=True, blank=True)
    linked_in = models.URLField(verbose_name='Linkedin', null=True, blank=True)
    tumblr = models.URLField(verbose_name='Tumblr', null=True, blank=True)
