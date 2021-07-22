"""
通过这条自定义指令启动apscheduler
python manage.py runapscheduler

"""
import logging

import requests
from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand, no_translations
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util

# logger = logging.getLogger(__name__)
from scheduler.models import Lottery

logger = logging.getLogger('django')


def my_job():
    # Your job processing logic here...
    logger.info('------： 每2小时执行了一次')
    payload = {'gameNo': 85, 'provinceId': 0, 'isVerify': 1, 'pageNo': 0, 'pageSize': 5}
    r = requests.get('https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry', params=payload)
    for i in r.json()['value']['list']:
        k = Lottery.objects.create(**i)
    pass


# The `close_old_connections` decorator ensures that database connections, that have become unusable or are obsolete,
# are closed before and after our job has run.
@util.close_old_connections
def delete_old_job_executions(max_age=604_800):
    """
    This job deletes APScheduler job execution entries older than `max_age` from the database. It helps to prevent the
    database from filling up with old historical records that are no longer useful.

    :param max_age: The maximum length of time to retain historical job execution records. Defaults
                    to 7 days.
    """
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "执行python manage.py runapscheduler 启动定时任务"

    @no_translations
    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")
        # scheduler.add_job(aps_test, 'interval', hours=1, jitter=120)
        scheduler.add_job(
            my_job,
            trigger=CronTrigger(hour="*/2"),  # Every 10 seconds
            id="my_job",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )
        self.stdout.write(self.style.SUCCESS('job已添加成功'))

        # scheduler.add_job(
        #     delete_old_job_executions,
        #     trigger=CronTrigger(
        #         day_of_week="mon", hour="00", minute="00"
        #     ),  # Midnight on Monday, before start of the next work week.
        #     id="delete_old_job_executions",
        #     max_instances=1,
        #     replace_existing=True,
        # )
        # logger.info(
        #     "Added weekly job: 'delete_old_job_executions'."
        # )

        try:
            self.stdout.write(self.style.SUCCESS('正在启动调度器...'))
            logger.info("运行日志: '正在启动调度器...'.")
            scheduler.start()
        except KeyboardInterrupt:
            self.stdout.write(self.style.SUCCESS('调度器正在终止...'))
            logger.info("运行日志: '调度器正在终止...'.")
            scheduler.shutdown()
            self.stdout.write(self.style.SUCCESS('调度器已终止！'))
            logger.info("运行日志: '调度器已终止'.")
