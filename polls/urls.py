from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import index

urlpatterns = [
    url(r'^$', 	index),
    url(r'^login/$', auth_views.login, {'template_name': 'polls/login.html'})
]
