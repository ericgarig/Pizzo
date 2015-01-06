from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

import datetime

def hello(request):
    return HttpResponse('Sup World')

def now(request):
    now = datetime.datetime.now()
    t = get_template('current_time.html')
    html = t.render(Context({'current_ts': now}))
    return HttpResponse(html)
    