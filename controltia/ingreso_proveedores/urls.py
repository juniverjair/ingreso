from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^get_reunion/$', views.get_reunion),
    url(r'^log/$', views.autologin),
]
