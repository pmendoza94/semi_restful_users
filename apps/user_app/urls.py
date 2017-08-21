from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^new$', views.new, name = 'new'),
    url(r'^create$', views.create, name = 'create'),
    url(r'^show/(?P<user_id>\d+)$', views.show, name = 'show'),
    url(r'^edit/(?P<user_id>\d+)$', views.edit, name = 'edit'),
    url(r'^update/(?P<user_id>\d+)$', views.update, name = 'update'),
    url(r'^destroy/(?P<user_id>\d+)$', views.destroy, name = 'destroy'),
]
