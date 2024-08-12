from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

# Create your views here.

week_schedule = {
    'Monday'    : 'Coding Practice',
    'Tuesday'   : 'Data Structures',
    'Wednesday' : 'Algorithms',
    'Thursday'  : 'Project Work',
    'Friday'    : 'Review and Planning',
}


def week(request,days):
    #return HttpResponse(month)

    day = list(week_schedule.keys())
    if(days>len(day)):
        return HttpResponseNotFound('weekend')
    redirect_days = day[days-1]
    redirect_path = reverse('week-detail',args=[redirect_days])

    return HttpResponseRedirect(redirect_path)

def week_details(request,days):
    try:
        week_text = week_schedule[days]
        return HttpResponse(week_text)
    except:
        return HttpResponseNotFound('Relax and Recharge')
