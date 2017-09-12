# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

def pay(request):
    return render(request, 'pay.html')

def commit(request):
    return HttpResponse('b')