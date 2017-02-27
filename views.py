from django.shortcuts import render
from .models import DateEntry, Date

import os
import datetime
import random

def index(request):
    today = datetime.datetime.now()
    #date = Date.objects.get(month=today.month, day=today.day)
    date = Date.objects.get(month=2, day=19)

    return for_date(request, date)

def for_date(request, date):

    entry = random.choice(DateEntry.objects.filter(date=date))

    return render(request, 'calendar_moe/index.html', {
        'entry': entry,
    })
