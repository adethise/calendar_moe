from django.shortcuts import render

import os
import datetime

def index(request):
    return date(request, datetime.datetime.now())

def date(request, date):
    #filename = '%d.%d.0.png' % (date.month, date.day)
    filename = '02.19.0.png'
    filepath = os.path.join('calendar_moe', filename)

    return render(request, 'calendar_moe/index.html', {
        'filepath': filepath,
    })
