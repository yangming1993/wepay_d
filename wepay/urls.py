from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.pay),
    url(r'^commit/$', views.commit)
]