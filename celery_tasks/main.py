from celery import Celery
celery_app = Celery('lg')
celery_app.config_from_object('celery_tasks.config')

# 注册任务
celery_app.autodiscover_tasks(['celery_tasks.sync_lottery_data'])
