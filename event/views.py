from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime, timezone
from .models import Event

#Variable to pass to year and month requirement in home()
#home() required 2 arguments as per events>utls.py
var_year = datetime.now().year
var_month = datetime.now().strftime('%B')


def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html',
                  {'event_list': event_list})


# Create your views here.
def home(request, year=var_year, month=var_month):
    name = "User Name"
    month = month.capitalize()
    #Convert month name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
    #Create Calander
    cal = HTMLCalendar().formatmonth(year, month_number)
    #Get Current Year
    now = datetime.now(timezone.utc)
    current_year = now.year
    #Get Current Time
    time = now.strftime('%I:%M %p')
    return render(
        request, 'events/index.html', {
            "name": name,
            "month": month,
            "year": year,
            "month_number": month_number,
            "cal": cal,
            "current_year": current_year,
            "time": time,
        })
