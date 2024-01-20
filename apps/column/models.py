from django.db import models

from apps.schema.models import Schema


class Column(models.Model):
    class ColumnTypeChoices(models.TextChoices):
        INT = 'int', 'Integer'
        FULL_NAME = 'full_name', 'Full name'
        EMAIL = 'email', 'Email'
        JOB = 'job', 'Job'
        DOMAIN_NAME = 'domain_name', 'domain_name'
        PHONE_NUMBER = 'phone_number', 'Phone number'
        COMPANY_NAME = 'company_name', 'Company name'
        TEXT = 'text', 'Text'
        ADDRESS = 'address', 'Address'
        DATE = 'date', 'Date'

    name = models.CharField('Column name', max_length=150)
    type = models.CharField('Column type', max_length=15, choices=ColumnTypeChoices.choices)
    params = models.JSONField('Params', null=True, blank=True)
    schema = models.ForeignKey(Schema, on_delete=models.SET_NULL, verbose_name='Schema', related_name='columns')

    def __str__(self):
        return f'{self.type} for schema {self.schema.name}'

    class Meta:
        verbose_name = 'Column'
        verbose_name_plural = 'Columns'
