from django.conf.urls import include, url
from apps.cart.views import CartAddView, CartInfoView

urlpatterns = [
    url(r'^add$', CartAddView.as_view(), name='add'),
    url(r'^$', CartInfoView.as_view(), name='show')
]
