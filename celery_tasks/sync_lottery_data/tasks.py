
"""
启动celery
celery -A celery_tasks.main worker -l info

"""
from celery import shared_task

from celery_tasks.main import celery_app


# @celery_app.task(name="sync_lottery_data")
@shared_task
def sum_two(x, y):
	"""两个数相加的异步任务"""
	return x + y
