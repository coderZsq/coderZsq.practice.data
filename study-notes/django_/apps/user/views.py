from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from apps.user.models import User
import re

# Create your views here.


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get('user_name')
        password = request.POST.get('pwd')
        email = request.POST.get('email')
        allow = request.POST.get('allow')

        if not all([username, password, email]):
            return render(request, 'register.html', {'errmgs': '数据不完整'})
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})
        if allow != 'on':
            return render(request, 'register.html', {'errmsg': '请同意协议'})

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = None

        if user:
            return render(request, 'register.html', {'errmsg', '用户名已存在'})

        user = User.objects.create_user(username, email, password)
        user.is_active = 0
        user.save()

        return redirect(reverse('goods:index'))


def register_handle(request):
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')
    allow = request.POST.get('allow')

    if not all([username, password, email]):
        return render(request, 'register.html', {'errmgs': '数据不完整'})
    if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
        return render(request, 'register.html', {'errmsg': '邮箱格式不正确'})
    if allow != 'on':
        return render(request, 'register.html', {'errmsg': '请同意协议'})

    # try:
    #     user = User.objects.get(username=username)
    # except User.DoesNotExist:
    #     user = None
    #
    # if user:
    #     return render(request, 'register.html', {'errmsg', '用户名已存在'})
    #
    # user = User.objects.create_user(username, email, password)
    # user.is_active = 0
    # user.save()

    return redirect(reverse('goods:index'))