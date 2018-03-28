from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps.users.v1.views import RegistrationView, KnoxLoginView,PasswordResetFixView
from .views import IndexView

v1_urls = ([
    url(r'^users/', include('apps.users.v1.urls', namespace='users')),
],"v1")

api_urls = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^auth/login/',KnoxLoginView.as_view(),name="knox_login_hi"),
    url(r'^auth/password/reset/$', PasswordResetFixView.as_view(), name="password_reset"),
    url(r'^auth/', include('knox.urls')),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration/$', RegistrationView.as_view(), name="rest_register"),
    url(r'^auth/registration/', include('rest_auth.registration.urls')),
    url(r'^allauth/', include('allauth.urls')),
    url(r'^drf-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^v1/', include(v1_urls,namespace="v1")),
]

urlpatterns = [
    url(r'^$', IndexView, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api_urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)