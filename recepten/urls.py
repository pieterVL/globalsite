from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^delete_post/(?P<topic_para>(.*))$', views.topic_post_delete, name='topic'),
    url(r'^delete/(?P<topic_para>(.*))$', views.topic_delete, name='topic'),
    # url(r'^(?P<topic_para>(.*))$', views.topic, name='topic'), #any character
    url(r'^(?P<topic_para>[0-z]+)', views.topic, name='topic'),
]