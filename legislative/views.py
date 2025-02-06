from django.shortcuts import render
from .services.legislative_service import LegislativeService

# Create your views here.

def home(request):
    service = LegislativeService()
    legislators = service.get_legislator_statistics()
    
    return render(request, 'legislative/home.html', {
        'legislators': legislators,
    })
