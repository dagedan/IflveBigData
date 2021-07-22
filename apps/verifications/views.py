import json

from django.http import HttpResponse, JsonResponse
from django.template.backends import django
from django.views import View
import re
from apps.verifications.libs.captcha.captcha import captcha
from django_redis import get_redis_connection
from . import contants


class ImgVerificationsView(View):
    def get(self, request, uuid):
        if re.match(r'([a-z0-9]+-?)+', uuid):
            text, image = captcha.generate_captcha()
            redis_conn = get_redis_connection('verify_code')
            redis_conn.setex('img_%s' % uuid, contants.IMAGE_CODE_REDIS_EXPIRSE, text)
            return HttpResponse(image, content_type='image/png')
        else:
            return HttpResponse({'success': 1, 'msg': '参数异常'})

    def post(self, request, uuid):
        client_code = json.loads(request.body)['code'].upper()
        redis_conn = get_redis_connection('verify_code')
        server_code = redis_conn.get('img_%s' % uuid).decode()
        if client_code == server_code:
            return JsonResponse({'success': 1, 'msg': '校验通过'})
        else:
            return JsonResponse({'success': 0, 'msg': '验证码错误或已过期'})
