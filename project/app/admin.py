# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import TestModel

# Register your models here.

@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):
    """
    """
