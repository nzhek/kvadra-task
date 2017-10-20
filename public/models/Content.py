from django.db import models


class Content(models.Model):
    txt = models.CharField(default="", max_length=100, verbose_name="Txt")

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'
