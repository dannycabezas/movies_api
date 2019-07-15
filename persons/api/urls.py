from django.urls import re_path

from persons.api import views

app_name = 'persons'
urlpatterns = [
    re_path(r'^$', views.PersonListAPIView.as_view(), name='list',),
    re_path(r'^(?P<pk>\d+)/$', views.PersonDetailAPIView.as_view(), name='detail', ),
    re_path(r'^(?P<pk>\d+)/edit/$', views.PersonUpdateAPIView.as_view(), name='update', ),
    re_path(r'^create/$', views.PersonCreateAPIView.as_view(), name='create'),
    re_path(r'^(?P<pk>\d+)/delete/$', views.PersonDeleteAPIView.as_view(), name='delete'),
]
