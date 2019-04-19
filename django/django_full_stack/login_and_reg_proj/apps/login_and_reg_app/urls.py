from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^create/$', views.create, name="create"),
    url(r'^login/$',views.login, name="login"),
    url(r'^success/$', views.show, name="show"),
    url(r'^logout/$',views.logout, name="logout"),
]
