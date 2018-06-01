from django.urls import re_path,path
from . import views
app_name='t1'
urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    path('register/',views.register,name='register'),
    re_path(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    #re_path(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite,name='favorite'),
    path('album/add/',views.AlbumCreate.as_view(),name='album-add'),
    re_path(r'album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(),name='album-update'),
    re_path(r'album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(),name='album-delete'),
]