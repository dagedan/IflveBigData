import logging

import requests
from django.core.management.base import BaseCommand, CommandError
from scheduler.models import Lottery

logger = logging.getLogger('django')


class Command(BaseCommand):
    help = '运行指令： python manag.py run_init_database 初始化开奖数据表'

    def handle(self, *args, **options):
        payload = {'gameNo': 85, 'provinceId': 0, 'isVerify': 1, 'pageNo': 1, 'pageSize': 5000}
        r = requests.get('https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry', params=payload)
        for i in r.json()['value']['list']:
            k = Lottery.objects.create(**i)
        self.stdout.write(self.style.SUCCESS('初始化数据完毕'))
