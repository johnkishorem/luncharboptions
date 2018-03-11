from django.conf.urls import url
from django.contrib.auth import views as auth_views
from polls.views import index,logout_view

urlpatterns = [
    url(r'^$', 	index),
    url(r'^login/$', auth_views.login, {'template_name': 'polls/login.html'}, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
]
