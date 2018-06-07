from django.conf.urls import include, url
from . import views
from multes.views import *

urlpatterns = [
    # url(r'^(?P<id>[0-9]+)$', views_multes.posa_multa, name="editar_multa"),
    url(r'^$', views.posa_multa, name='posa_multa'),
   url(r'^(?P<pk>[0-9]+)/$', views.craft_detail, name='craft_detail'),
   url(r'^new/$', views.craft_new, name='craft_new'),
   url(r'^post/(?P<pk>[0-9]+)/edit/$', views.craft_edit, name='craft_edit'),
   url(r'^drafts/$', views.craft_draft_list, name='craft_draft_list'),
   url(r'^post/(?P<pk>[0-9]+)/publish/$', views.craft_publish, name='craft_publish'),
   url(r'^post/(?P<pk>[0-9]+)/remove/$', views.craft_remove, name='craft_remove'),
   # url(r'^post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_craft, name='add_comment_to_craft'),
   url(r'^comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
   url(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),
]
