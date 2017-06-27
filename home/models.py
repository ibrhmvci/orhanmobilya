from django.db import models


class SliderImage(models.Model):
    photo = models.ImageField(blank=False, null=False, upload_to='slider-images')
    title = models.CharField(max_length=250)
    link1 = models.CharField(max_length=250)
    link1_title = models.CharField(max_length=25)
    link2 = models.CharField(max_length=250)
    link2_title = models.CharField(max_length=25)

    def __str__(self):
        return self.title

