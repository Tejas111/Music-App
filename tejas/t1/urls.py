from django.urls import re_path,path
from . import views
app_name='t1'
urlpatterns=[
    path('',views.ind),
    re_path(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail'),
    re_path(r'^(?P<album_id>[0-9]+)/favorite/$',views.favorite,name='favorite'),

]