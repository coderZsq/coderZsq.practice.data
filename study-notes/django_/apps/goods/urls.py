from django.conf.urls import url
from apps.goods.views import IndexView

urlpatterns = [
    url(r'^index$', IndexView.as_view(), name='index')
]
