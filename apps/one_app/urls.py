from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<id>\d+)$', views.blog_number),
    url(r'^(?P<id>\d+)/edit$', views.blog_number_edit),
    url(r'^(?P<id>\d+)/delete$', views.destroy),
]