from django.db import models

from apps.user.models import User


class Schema(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='schemas')
    name = models.CharField('Name', max_length=150)
    number_of_records = models.SmallIntegerField('Number of records', default=1)

    def __str__(self):
        return f'Schema {self.name}'

    class Meta:
        verbose_name = 'Schema'
        verbose_name_plural = 'Schemas'
        ordering = ['name']
