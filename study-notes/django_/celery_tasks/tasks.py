from django.core.mail import send_mail
from django.conf import settings
from celery import Celery

import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_.settings")
django.setup()

app = Celery('celery_tasks.tasks', broker='redis://127.0.0.1:6379/1')
# celery -A celery_tasks.tasks worker --loglevel=info

from django.template import loader, RequestContext
from apps.goods.models import GoodsType, IndexGoodsBanner, IndexPromotionBanner, IndexTypeGoodsBanner
# from celery_tasks.tasks import generate_static_index_html
# generate_static_index_html.delay()
# <AsyncResult: 10e95aad-4c4e-4306-8dd1-a5571171956e>


@app.task
def send_register_active_email(to_email, username, token):
    subject = '邮件主题'
    message = '邮件正文'
    sender = settings.EMAIL_FROM
    receiver = [to_email]
    html_message = '%s, 点击链接 -> <a href="http://localhost:8000/user/active/%s">http://localhost:8000/user/active/%s</a>' % (
    username, token, token)
    send_mail(subject, message, sender, receiver, html_message=html_message)


@app.task
def generate_static_index_html():
    types = GoodsType.objects.all()
    goods_banners = IndexGoodsBanner.objects.all().order_by('index')
    promotion_banners = IndexPromotionBanner.objects.all().order_by('index')
    for type in types:
        image_banners = IndexTypeGoodsBanner.objects.filter(type=type, display_type=1).order_by('index')
        title_banners = IndexTypeGoodsBanner.objects.filter(type=type, display_type=0).order_by('index')
        type.image_banners = image_banners
        type.title_banners = title_banners
    context = {
        'types': types,
        'goods_banners': goods_banners,
        'promotion_banners': promotion_banners
    }
    temp = loader.get_template('static_index.html')
    static_index_html = temp.render(context)
    save_path = os.path.join(settings.BASE_DIR, 'static/index.html')
    with open(save_path, 'w') as f:
        f.write(static_index_html)