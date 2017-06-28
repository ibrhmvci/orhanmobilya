from django.conf.urls import url
from .views import post_detail

app_name = 'post'

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
]