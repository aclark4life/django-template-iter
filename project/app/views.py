# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import TestModel
from collections import OrderedDict

# Create your views here.

def home(request):
    context = {}
    items = TestModel.objects.all()
    for item in items:
        fields = item._meta._get_fields()
        item.fields = OrderedDict()
        for field in fields:
            item.fields[field.name] = getattr(item, field.name)
    context['items'] = items
    return render(request, 'base.html', context) 
