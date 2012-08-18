'''
Created on 2011-8-5

@author: Administrator
'''
from django.http import HttpResponse,Http404
import datetime

def hello(request):
    return  HttpResponse("  hello  robber..")

def current_time(request):
    now=datetime.datetime.now()
    return HttpResponse(get_html_str(now));


def plustime(request,diff):
    print diff+"---------------------"
    try:
        diff=int(diff)
    except ValueError:
        raise Http404()
    return HttpResponse(get_html_str(datetime.datetime.now()+datetime.timedelta(hours=diff)));


def plusdays(request,diff):
    print diff+"---------------------"
    try:
        diff=int(diff)
    except ValueError:
        raise Http404()
    return HttpResponse(get_html_str(datetime.datetime.now()+datetime.timedelta(days=diff)));
    
    
    
    
def  get_html_str(var):
    return "<html><body> the result time is %s..</body></html>"%var
        
    
    