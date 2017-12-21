"""dating URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# from django.views.generic import RedirectView
from account import views
#import notifications.urls




urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    # url(r'^(/)?$', RedirectView.as_view(url='/account/login/')),
    url(r'^account/',include('account.urls')),
    url(r'^search/', include('search.urls')),
    url(r'^messages/', include('django_messages.urls')),
    url(r'^friendship/', include('friendship.urls')),
    url(r'^social-auth/',include('social.apps.django_app.urls')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    # url(r'^notifications/', include('pinax.notifications.urls', namespace='pinax_notifications')),
    # url(r'', include('django_private_chat.urls')),
    # url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
