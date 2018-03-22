from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/$', views.TxtList.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.TxtDetail.as_view()),
]
