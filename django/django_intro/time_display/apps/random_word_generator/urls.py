from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^random_word$',views.display),
    url(r'^random_words/reset$',views.reset),
]