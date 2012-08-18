
from django.http import HttpResponse,Http404
from django.template.loader import get_template
from django.template import Template,Context
from django.shortcuts import render_to_response
import datetime



def current_time(request):
    now=datetime.datetime.now()
    t=Template("<html><body> it is now {{time}}</body></html>")
    c=Context({'time':now})
    return HttpResponse(t.render(c))


def current_ttime(request):
    now=datetime.datetime.now()
    t=get_template("time/currentTime1.html")
    return HttpResponse(t.render(Context({'time':now})))

#locals() include all the inner var,,var's name must be the same as the file
def render_res_current_time(request):
    now=datetime.datetime.now()
    return render_to_response("time/currentTime.html",{'time':now})


def plus_days(request,days_offset):
    try:
        days_offset=int(days_offset)
    except ValueError:
        raise Http404()
    now=datetime.datetime.now()+datetime.timedelta(days=days_offset)
    return render_to_response("time/adddays.html",{'time':now,"days_offset":days_offset})
    
#def plustime(request,diff):
#    print diff+"---------------------"
#    try:
#        diff=int(diff)
#    except ValueError:
#        raise Http404()
#    return HttpResponse(get_html_str(datetime.datetime.now()+datetime.timedelta(hours=diff)));
#
#
#def plusdays(request,diff):
#    print diff+"---------------------"
#    try:
#        diff=int(diff)
#    except ValueError:
#        raise Http404()
#    return HttpResponse(get_html_str(datetime.datetime.now()+datetime.timedelta(days=diff)));
#    
#    
#    
#    
#def  get_html_str(var):
#    return "<html><body> the result time is %s..</body></html>"%var
        
    
    