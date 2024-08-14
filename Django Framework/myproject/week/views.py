from django.shortcuts import render,reverse
from django.http import *
# Create your views here.

week_days = {
    'mon' : "Test in Python",
    'tue' : "Test in React",
    'wed' : "Test in Angular",
    'thur' : "Test in .Net",
    'fri' : "Test in FunFriday",
    'sat' : "Rest",
    'sun' : "Rest",
}

def week_Details(request,week):
    try:
        week_day = week_days[week]
        return HttpResponse(week_day)
    except:
        return HttpResponseNotFound('Not Found')
    
def week_details_num(request,week):
    week_day_list = list(week_days.keys())
    if week > len(week_day_list):
        return HttpResponseNotFound('Not Found')
    week_day = week_day_list[week-1]
    week_day = reverse('week_detail',args=[week_day])
    return HttpResponseRedirect(week_day)

def index(request):
    week_list = list(week_days.keys())

    return render(request,)