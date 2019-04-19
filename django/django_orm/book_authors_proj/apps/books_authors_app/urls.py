from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^authors$',views.authors),
    # books/book_id/show = view books page
    url(r'books/(?P<book_id>\d+)$',views.books),
    url(r'author/(?P<author_id>\d+)$',views.author),
    # books/create  = add_book
    url(r'add_book$', views.add_book),
    url(r'add_book_to_author$',views.add_book_to_author),
    url(r'add_new_author$',views.add_new_author),
    url(r'add_author_to_book$',views.add_author_to_book),

]