from django.urls import re_path,path
from . import views
app_name='t1'
urlpatterns=[
    path('',views.IndexView.as_view(),name='index'),
    re_path(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name='detail'),
    #re_path(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite,name='favorite'),

]