from django.conf.urls import url, include
from django.contrib import admin
from home.views import index_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view, name='index'),

]


