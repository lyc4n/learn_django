from django.conf.urls import url
from todos import views

urlpatterns = [
    url(r'^$', views.index, name='todos_index'),
    url(r'^finish_todo/(\d+)/$', views.finish, name='todo_finish'),
    url(r'^unfinish_todo/(\d+)/$', views.unfinish, name='todo_unfinish'),
    url(r'^create_todo/', views.create, name='todo_create'),
    url(r'^destroy_todo/(\d+)/$', views.destroy, name='todo_destroy'),
]
