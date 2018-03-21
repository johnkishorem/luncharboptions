from django.conf.urls import url
from django.contrib.auth import views as auth_views
from polls.views import index_view,logout_view,vote_view,register_view

app_name = 'polls'
urlpatterns = [
    url(r'^$', 	index_view, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'polls/login.html'}, name='login'),
    url(r'^register/$', register_view, name='register'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^vote/$', vote_view, name='vote'),
]
