from django.conf.urls import url
from django.views.generic.base import TemplateView

from . import views

app_name = "movies"

urlpatterns = [

	# API URLS
    #---------#
    # /api/
    url(r'^api/$', views.ApiIndexView.as_view(), name='apiindex'),
    # /api/list/
    url(r'^api/list/$', views.ApiListView.as_view(), name='apilist'),
    # /api/424/
    url(r'^api/(?P<pk>[0-9]+)/$', views.ApiDetailView.as_view(), name='apidetail'),
    #---------#

    # /
    url(r'^.*$', TemplateView.as_view(template_name='movies/index.html'), name='index'),

]