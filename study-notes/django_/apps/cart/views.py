from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from apps.goods.models import GoodsSKU
from django_redis import get_redis_connection
from utils.mixin import LoginRequiredMixin

# Create your views here.


class CartAddView(View):
    @staticmethod
    def post(request):
        user = request.user
        if not user.is_authenticated():
            return JsonResponse({'res': 0, 'errmsg': '请先登录'})
        sku_id = request.POST.get('sku_id')
        count = request.POST.get('count')
        if not all([sku_id, count]):
            return JsonResponse({'res': 1, 'errmsg': '数据不完整'})
        try:
            count = int(count)
        except Exception as e:
            return JsonResponse({'res': 2, 'errmsg': '商品数目出错'})
        try:
            sku = GoodsSKU.objects.get(id=sku_id)
        except GoodsSKU.DoesNotExist:
            return JsonResponse({'res': 3, 'errmsg': '商品不存在'})
        conn = get_redis_connection('default')
        cart_key = 'cart_%d' % user.id
        cart_count = conn.hget(cart_key, sku_id)
        if cart_count:
            count += int(cart_count)
        if count > sku.stock:
            return JsonResponse({'res': 4, 'errmsg': '商品库存不足'})
        conn.hset(cart_key, sku_id, count)
        total_count = conn.hlen(cart_key)
        return JsonResponse({'res': 5, 'total_count': total_count, 'message': '添加成功'})


class CartInfoView(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        user = request.user
        conn = get_redis_connection('default')
        cart_key = 'cart_%d' % user.id
        cart_dict = conn.hgetall(cart_key)
        skus = []
        total_count = 0
        total_price = 0
        for sku_id, count in cart_dict.items():
            sku = GoodsSKU.objects.get(id=sku_id)
            amount = sku.price * int(count)
            sku.amount = amount
            sku.count = count
            skus.append(sku)
            total_count += int(count)
            total_price += amount
        context = {'total_count': total_count,
                   'total_price': total_price,
                   'skus': skus}
        return render(request, 'cart.html', context)