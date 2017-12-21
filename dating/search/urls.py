from django.conf.urls import url
from . import views
from django.views.decorators.cache import never_cache

app_name = 'search'
urlpatterns = [
	url(r'^$', never_cache(views.search), name = 'search'),
	url(r'^result/$', views.searchresult, name='searchresult'),
]
