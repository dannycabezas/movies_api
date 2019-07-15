from django.urls import re_path

from movies.api import views

app_name = 'movie'

urlpatterns = [
    re_path(r'^$', views.MovieListAPIView.as_view(), name='list',),
    re_path(r'^(?P<pk>\d+)/$', views.MovieDetailAPIView.as_view(), name='detail', ),
    re_path(r'^(?P<pk>\d+)/edit/$', views.MovieUpdateAPIView.as_view(), name='update', ),
    re_path(r'^create/$', views.MovieCreateAPIView.as_view(), name='create'),
    re_path(r'^(?P<pk>\d+)/delete/$', views.MovieDeleteAPIView.as_view(), name='delete'),
]
