from django.shortcuts import render,reverse
from django.http import *
from django.templete.loader import render_to_string
# Create your views here.

month_schedule = {
    'jan' : 'Learning Python',
    'feb' : 'Learning Java',
    'mar' : 'Learning .Net',
    'aprl' : 'Learning React',
}

def monthly_details_num(request,month):
    months = list(month_schedule.keys())
    if (month > len(months)):
        return HttpResponseNotFound('Request is Not Found')
    else:
        redirect_month = months[month-1]
    # month_text = month_schedule[month_key]
        redirect_path = reverse('month-detail',args=[redirect_month])
        return HttpResponseRedirect(redirect_path)


def monthly_details(request,month):
    try:
        month_text = month_schedule[month]
        responce_data = render_to_string('month_details')
        return HttpResponse(f'<h1>{month_text}</h1>')
    except:
        return HttpResponseNotFound('This is not Mentioned')

def index(request):
    return HttpResponse("This Works!")

