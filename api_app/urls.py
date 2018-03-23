from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/$', views.TxtList.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.TxtDetail.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
