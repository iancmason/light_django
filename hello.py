from django.conf import settings

settings.configure(
    DEBUG=True,
    SECRET_KEY='THISISTHESECRETKEY',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)

from django.conf.urls import url
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello World')

urlpatterns = (
    url(r'^$', index),
)
