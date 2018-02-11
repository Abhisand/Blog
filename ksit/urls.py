
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from blog import views as blog_views


urlpatterns = [
    url(r'^post/$',blog_views.post),
    url(r'^$',blog_views.index),
    url('admin/', admin.site.urls),
]
