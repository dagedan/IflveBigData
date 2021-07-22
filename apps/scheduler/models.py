from django.db import models

# Create your models here.
from django.db.models import Model


class Lottery(Model):
	lotteryGameName = models.CharField(max_length=255)
	drawFlowFund = models.CharField(max_length=255)
	drawFlowFundRj = models.CharField(max_length=255)
	estimateDrawTime = models.CharField(max_length=255)
	isGetKjpdf = models.IntegerField()
	isGetXlpdf = models.IntegerField()
	lotteryDrawNum = models.CharField(max_length=255)
	lotteryDrawResult = models.CharField(max_length=255)
	lotteryDrawResult = models.CharField(max_length=255)
	lotteryDrawStatus = models.IntegerField()
	lotteryDrawTime = models.CharField(max_length=255)
	lotteryEquipmentCount = models.IntegerField()
	lotteryGameNum = models.CharField(max_length=255)
	lotteryGamePronum = models.IntegerField()
	lotteryPaidBeginTime = models.CharField(max_length=255)
	lotteryPaidEndTime = models.CharField(max_length=255)
	lotteryPromotionFlag = models.IntegerField()
	lotterySaleBeginTime = models.CharField(max_length=255)
	lotterySaleEndTimeUnix = models.IntegerField()
	lotterySaleEndtime = models.CharField(max_length=255)
	lotterySuspendedFlag = models.IntegerField()
	lotteryUnsortDrawresult = models.CharField(max_length=255)
	matchList = models.JSONField()
	pdfType = models.IntegerField()
	poolBalanceAfterdraw = models.CharField(max_length=255)
	poolBalanceAfterdrawRj = models.CharField(max_length=255)
	prizeLevelList = models.JSONField()
	prizeLevelListRj = models.JSONField()
	ruleType = models.IntegerField()
	termList = models.JSONField()
	totalSaleAmount = models.CharField(max_length=255)
	totalSaleAmountRj = models.CharField(max_length=255)
	verify = models.IntegerField()
	vtoolsConfig = models.JSONField()

	class Meta:
		db_table = 'lottery_history'
		verbose_name = "开奖历史数据"
		verbose_name_plural = verbose_name

	def __str__(self):
		return self.lotteryGameName
