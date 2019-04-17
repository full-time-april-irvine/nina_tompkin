from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.display_time),
    url(r'^time_display$',views.display_time),
]