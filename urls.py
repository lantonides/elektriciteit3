from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'bereken$', views.bereken, name='bereken'),
]

