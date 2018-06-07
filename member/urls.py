from django.conf.urls import url

from . import views

# from member.views import SignDoneTV

urlpatterns = [
	# url(r'^signup/done/$', SignDoneTV.as_view(), name='register_done'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
]