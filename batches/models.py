from django.db import models


class Kawase(models.Model):
    """為替Test"""
    update = models.DateTimeField('更新日')
    jpy = models.FloatField('JPY')

    def __str__(self):
        return self.name


class BitTest(models.Model):
    """BitTest"""
    bidExchangeName = models.CharField('bidExchangeName',max_length=255)
    bidPrice = models.FloatField('bidPrice')
    askExchangeName = models.CharField('askExchangeName',max_length=255)
    askPrice = models.FloatField('askPrice')
    createDate = models.DateTimeField('作成日')

    def __str__(self):
        return self.name
