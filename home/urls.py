from django.conf.urls import url
from .views import *

urlpatterns = [

    url(r'^index/', index_view, name='index'),

]