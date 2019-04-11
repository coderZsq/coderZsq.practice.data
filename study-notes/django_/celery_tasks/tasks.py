from django.core.mail import send_mail
from django.conf import settings
# from celery import Celery

# import os
# import django
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_.settings")
# django.setup()

# app = Celery('celery_tasks.tasks', broker='redis://localhost:6379/')


# @app.task
def send_register_active_email(to_email, username, token):
    subject = '邮件主题'
    message = '邮件正文'
    sender = settings.EMAIL_FROM
    receiver = [to_email]
    html_message = '%s, 点击链接 -> <a href="http://localhost:8000/user/active/%s">http://localhost:8000/user/active/%s</a>' % (
    username, token, token)
    send_mail(subject, message, sender, receiver, html_message=html_message)