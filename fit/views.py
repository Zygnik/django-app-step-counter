from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Date, Steps
from django.template import loader
from django.http import Http404
from django.urls import reverse
import datetime, json


def index(request):
    return render(request, 'fit/index.html', {'date': Date})

def stepsAdded(request):
    # Read date and steps submitted by form on index.html, 
    # save them to database and pass them to stepsAdded.html
    try:
        dateValue = request.POST['dateValue']
        steps = request.POST['numberValue']
    except (KeyError, Date.DoesNotExist):
        return render(request, 'fit/index.html', {
            'date': Date,
            'error_message': "Something went wrong.",
        })
    else:
        dateObject = Date.objects.create(date=datetime.datetime.strptime(dateValue, "%d/%m/%Y").date())
        stepsObject = Steps.objects.create(date=dateObject, number_of_steps=steps)
        context={}
        context['date']=dateObject
        context['steps']=stepsObject
        return render(request, 'fit/stepsAdded.html', context=context)

def results(request):
    # Read date range subimitted by form on index.html and retrive data from database
    # between this date range
    try:
        dateRange = request.POST['dateRange']
    except (KeyError, Date.DoesNotExist):
        return render(request, 'fit/index.html', {
            'date': Date,
            'error_message': "Something went wrong.",
        })
    else:
        #Split date range values and filter database for this range
        datesLimits=dateRange.split(" - ")
        datesObjects=Date.objects.filter(date__range=[datetime.datetime.strptime(datesLimits[0], "%d/%m/%Y").date(), 
                                                datetime.datetime.strptime(datesLimits[1], "%d/%m/%Y").date()])
        dates=Date.objects.filter(date__range=[datetime.datetime.strptime(datesLimits[0], "%d/%m/%Y").date(), 
                                                datetime.datetime.strptime(datesLimits[1], "%d/%m/%Y").date()]).values('date')
        query=[]
        # Calculate with the help of dateObjects var the Steps model elements that 
        # are connected with each date retrieved from previous filter function
        for d in datesObjects:
            query.append(d.steps_set.all().values_list('number_of_steps', flat=True).distinct())
        stepsRange=[]
        # Retrieve the value of steps from QuerySet list
        for q in query:
            stepsRange.append(q[0])
        context={}
        context['dates']= dates
        context['stepsRange']=stepsRange
        return render(request, 'fit/results.html', context=context)