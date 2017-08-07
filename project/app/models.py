# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TestModel(models.Model):
    """
    """
    field_1 = models.CharField(max_length=300, blank=True, null=True)
    field_2 = models.CharField(max_length=300, blank=True, null=True)
    field_3 = models.CharField(max_length=300, blank=True, null=True)
