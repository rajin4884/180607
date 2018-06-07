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
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from mysite.views import HomeView
from . import views
# from mysite.views import UserCreateView, UserCreateDoneTV
from mysite.views import UserCreateDoneTV
# from multes import views as views_multes
from multes import views as views_persones
# from mentoring import views as views_mentoring

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^accounts/', include('django.contrib.auth.urls')),
    # url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    # url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),
    url(r'^member/', include('member.urls', namespace='member')),
    url(r'^board/',  include('board.urls', namespace='board')),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^photo/', include('photo.urls', namespace='photo')),
    # url(r'^mentoring/', include('mentoring.urls', namespace='mentoring')),
    url(r'^multes/',  include('multes.urls', namespace='multes')),
    # url(r'^editar_multa/', views_multes.posa_multa, name="editar_multa"),
    url(r'^persones-api$', views_persones.persones_api, name="persones_api"),
    url(r'^companys/', include('companys.urls', namespace='companys')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
