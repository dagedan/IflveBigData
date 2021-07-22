from django.db.models import Max
from django.shortcuts import render
from celery_tasks.sync_lottery_data.tasks import sum_two
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job


# Create your views here.
from django.views import View
from scheduler.models import Lottery


class IndexView(View):
	def get(self, request):
		newestLottery = Lottery.objects.order_by("-lotteryDrawNum")[0]
		# newestLottery = Lottery.objects.aggregate(Max('lotteryDrawNum'))
		print(newestLottery)
		content ={
			'newestLottery': newestLottery
		}
		return render(request, 'index.html', context=content)
		# return render(request, 'index.html', context={'foo': 'bar'})
