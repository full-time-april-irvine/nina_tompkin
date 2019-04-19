from django.conf.urls import url
from . import views

urlpatterns = [
    #1 url that renders the template for showing all of the shows
    url(r'^$', views.index, name="index"),
    # 2 url that renders the template for adding a new show
    url(r'^new/$', views.new, name="new"),
    #3 url that processes the addition of a new show and redirects to the page that shows the new show
    url(r'^create/$', views.create, name="create"),
    #4 url that renders the template that displays a single, selected show
    url(r'^(?P<show_id>\d+)/$', views.show, name="show"),
    #5 url that renders the template for editing an existing show
    url(r'^(?P<show_id>\d+)/edit/$', views.edit, name="edit"),
    #6 url that processes the updating of an existing record and redirects to the show's individual page
    url(r'^(?P<show_id>\d+)/update/$', views.update, name="update"),
    #7 url that processes the deletion of a record and redirects to the main show page
    url(r'^(?P<show_id>\d+)/delete/$', views.destroy, name="destroy"),

]