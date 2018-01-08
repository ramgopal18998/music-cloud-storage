from django.conf.urls import url
from . import views
from django.contrib.auth.views import (
    password_reset, password_reset_done, password_reset_confirm,
    password_reset_complete
)
app_name = 'music'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<album_id>[0-9]+)/update/$', views.update, name='album-update'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
    url(r'^create_album/$', views.create_album, name='create_album'),
    url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
    url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),
    url(r'^password/$', views.change_password, name='change_password'),

    #reset-password
    url(r'^reset-password$',password_reset,{'template_name':'music/password/reset_password.html','post_reset_redirect':'music:password_reset_done','email_template_name': 'music/password/reset_password_email.html'},name='reset_password'),
    url(r'^reset-password/done/$', password_reset_done, {'template_name': 'music/password/reset_password_done.html'}, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'music/password/reset_password_confirm.html', 'post_reset_redirect': 'music:password_reset_complete'}, name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete,{'template_name': 'music/password/reset_password_complete.html'}, name='password_reset_complete'),
]
