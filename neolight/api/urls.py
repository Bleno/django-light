from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^$', views.snippet_list),
    url(r'^(?P<name>[^/]+)/$', views.snippet_detail),
]
