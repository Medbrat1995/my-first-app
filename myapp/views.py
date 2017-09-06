from django.shortcuts import render
from .models import Vehicle, TipperModel

def vehicle_list(request):
	vehicles = Vehicle.objects.all()
	tippermodels = TipperModel.objects.all()
	value = request.GET.get("filter")
	if(value == "all"):
		filtered = vehicles
	else:
		filtered = Vehicle.objects.filter(model__model_name = value)
	return render(request, 'myapp/vehicle_list.html',{'vehicles': vehicles, 'tippermodels': tippermodels, 'filtered': filtered})
	
	
