from django.conf.urls import url
from django.conf import settings
from django.contrib.staticfiles import views
from . import views as myappServe

urlpatterns = [
	url(r'$', myappServe.vehicle_list, name='vehicle_list'),
]

if settings.DEBUG:
	urlpatterns += [
		url(r'^static/(?P<path>.*)$', views.serve),
	]
	