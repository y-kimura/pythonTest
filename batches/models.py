from django.db import models


class Kawase(models.Model):
    """為替Test"""
    update = models.DateTimeField('更新日')
    jpy = models.FloatField('JPY')

    def __str__(self):
        return self.name