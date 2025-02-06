from django.shortcuts import render
from .services.legislative_service import LegislativeService


def home(request):
    service = LegislativeService()
    legislators = service.get_legislator_statistics()
    bills_analysis = service.get_bills_analysis()
    
    return render(request, 'legislative/home.html', {
        'legislators': legislators,
        'bills_analysis': bills_analysis,
    })
