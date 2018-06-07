from django.conf.urls import include, url
from board import views
from board.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [

    url(r'^$', views.home, name = 'index'),
    url(r'^show_write_form/$', views.show_write_form, name='show_write_form'),
    url(r'^DoWriteBoard/$', views.DoWriteBoard, name='DoWriteBoard'),
    url(r'^viewWork/$', views.viewWork, name='viewWork'),
    # url(r'^/listSpecificPageWork/$', views.listSpecificPageWork, name='listSpecificPageWork'),
    url(r'^listSpecificPageWork_to_update/$', views.listSpecificPageWork_to_update, name='listSpecificPageWork_to_update'),
    url(r'^updateBoard/$', views.updateBoard, name='updateBoard'),
    url(r'^DeleteSpecificRow/$', views.DeleteSpecificRow, name='DeleteSpecificRow'),
    url(r'^searchWithSubject/$', views.searchWithSubject, name='searchWithSubject'),
    # url(r'^/listSearchedSpecificPageWork/$', views.listSearchedSpecificPageWork, name='listSpecificPageWork'),



]
