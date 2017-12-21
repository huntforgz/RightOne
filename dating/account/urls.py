from django.conf.urls import url
from . import views
from django.views.decorators.cache import never_cache
from django.contrib.auth import views as auto_views

urlpatterns = [
    # post views
    url(r'^login/$', auto_views.login, name='login'),
    url(r'^logout/$', auto_views.logout, name='logout'),
    url(r'^logout-then-login/$', auto_views.logout_then_login, name='logout_then_login'),
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^password-change/$', auto_views.password_change, name='password_change'),
    url(r'^password-change/done/$',auto_views.password_change_done, name='password_change_done'),
    url(r'^password-reset/$',auto_views.password_reset,name='password_reset'),
    url(r'^password-reset/done/$',auto_views.password_reset_done,name='password_reset_done'),
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',auto_views.password_reset_confirm,name='password_reset_confirm'),
    url(r'^password-reset/complete/$',auto_views.password_reset_complete,name='password_reset_complete'),
    url(r'^register/$', views.register, name='register'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^profile/$', views.viewprofile, name='viewprofile'),
    url(r'^profile/(?P<pk>\d+)/$', views.viewprofile, name='view_profile_with_pk'),
    url(r'^profile/(?P<username>\w+)/$', views.viewprofilewithname, name='view_profile_with_name'),
    # Profile self View
    # url(r'^$', never_cache(ProfileView.as_view()), name="sp_profile_view_page"),
    # #
    # # # Profile Other View
    # url(r'^view/(?P<username>\w+)/$',ProfileView.as_view(), name="sp_profile_other_view_page"),
]
