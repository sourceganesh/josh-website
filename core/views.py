from django.shortcuts import render
from core.models import EventsList

# Create your views here.
def index_view(request):

    events_list = EventsList.objects.all().order_by('participants').filter(participants__lte=50)
    
    context = { 'owner' : 'ganesh', 'events_list' : events_list }

    return render(request, 'index.html', context= context)