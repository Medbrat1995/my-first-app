from django.shortcuts import render
from .models import Vehicle, TipperModel

def vehicle_list(request):
	vehicles = Vehicle.objects.all()
	return render(request, 'myapp/vehicle_list.html',{'vehicles': vehicles})
	
	
