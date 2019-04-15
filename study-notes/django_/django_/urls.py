from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'django_.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')), # 富文本编辑器
    url(r'^search', include('haystack.urls')), # 全文检索框架
    url(r'^user/', include('user.urls', namespace='user')), # 用户模块
    url(r'^cart/', include('cart.urls', namespace='cart')), # 购物车模块
    url(r'^order/', include('order.urls', namespace='order')), # 订单模块
    url(r'^', include('goods.urls', namespace='goods')), # 商品模块
]
