"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from companys.views import *
from .models import Pay
from . import views
urlpatterns = [
    # Example: /
    url(r'^$', CompanysLV.as_view(), name='index'),

    url(r'^success/$', views.success, name = 'success'),
    # Example: /post/ (same as /)
    url(r'^companys/$', CompanysLV.as_view(), name='companys_list'),

    # Example: /post/django-example/
    url(r'^(?P<slug>[-\w]+)/$', CompanysDV.as_view(), name='companys_detail'),

    # Example: /archive/
    # url(r'^archive/$', CompanysAV.as_view(), name='post_archive'),
    #
    # # Example: /2012/
    # url(r'^(?P<year>\d{4})/$', CompanysYAV.as_view(), name='post_year_archive'),
    #
    # # Example: /2012/nov/
    # url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', CompanysMAV.as_view(), name='post_month_archive'),
    #
    # # Example: /2012/nov/10/
    # url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', CompanysDAV.as_view(), name='post_day_archive'),
    #
    # # Example: /today/
    # url(r'^today/$', CompanysTAV.as_view(), name='post_today_archive'),

    # Example: /tag/
    # url(r'^tag/$', TagTV.as_view(), name='tag_cloud'),
    #
    # # Example: /tag/tagname/
    # url(r'^tag/(?P<tag>[^/]+(?u))/$', PostTOL.as_view(), name='tagged_object_list'),

    # Example: /search/
    url (r'^search/$', SearchFormView.as_view(), name='search'),

    # Example: /add/
    url(r'^add/$',
        CompanysCreateView.as_view(), name="add",
    ),

    # Example: /change/
    url(r'^change/$',
        CompanysChangeLV.as_view(), name="change",
    ),

    # Example: /99/update/
    url(r'^(?P<pk>[0-9]+)/update/$',
        CompanysUpdateView.as_view(), name="update",
    ),

    # Example: /99/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$',
        CompanysDeleteView.as_view(), name="delete",
    ),
    #
    # """
    # 앨범/사진
    # """
    # # Example: /photo/99/
    # url(r'^photo/(?P<pk>\d+)/$', PhotoDV.as_view(), name='photo_detail'),
    #
    # # Example: /album/add/
    # url(r'^album/add/$',
    #     AlbumPhotoCV.as_view(), name="album_add",
    # ),
    #
    # # Example: /album/change/
    # url(r'^album/change/$',
    #     AlbumChangeLV.as_view(), name="album_change",
    # ),
    #
    # # Example: /album/99/update/
    # url(r'^album/(?P<pk>[0-9]+)/update/$',
    #     AlbumPhotoUV.as_view(), name="album_update",
    # ),
    #
    # # Example: /album/99/delete/
    # url(r'^album/(?P<pk>[0-9]+)/delete/$',
    #     AlbumDeleteView.as_view(), name="album_delete",
    # ),
    #
    # # Example: /photo/add/
    # url(r'^photo/add/$',
    #     PhotoCreateView.as_view(), name="photo_add",
    # ),
    #
    # # Example: /photo/change/
    # url(r'^photo/change/$',
    #     PhotoChangeLV.as_view(), name="photo_change",
    # ),
    #
    # # Example: /photo/99/update/
    # url(r'^photo/(?P<pk>[0-9]+)/update/$',
    #     PhotoUpdateView.as_view(), name="photo_update",
    # ),
    #
    # # Example: /photo/99/delete/
    # url(r'^photo/(?P<pk>[0-9]+)/delete/$',
    #     PhotoDeleteView.as_view(), name="photo_delete",
    # ),


    # Example: /test/
    #url(r'^test/$', TestPostLV.as_view(), name='post_test'),
    # Example: /test/word/
    url(r'^test/(?P<word>[\w]+)/$', TestCompanysLV.as_view(), name='post_test'),
]
