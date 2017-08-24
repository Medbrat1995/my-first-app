from django.db import models
from django.db.models import F


class TipperModel(models.Model):
	model_name = models.CharField(max_length=20, primary_key=True)
	max_weight = models.FloatField()

def add_tipper_model(self):
	self.save()
  

class Vehicle(models.Model):
	vehicle_number = models.CharField(max_length=10, primary_key=True)
	vehicle_model = models.ForeignKey(TipperModel)
	current_weight = models.FloatField()
	vehicle_overweight = models.FloatField(editable=False, default=0.0)
	

def add(vehicle_number, vehicle_model, current_weight):
	item=models.vehicle()
	item.vehicle_number=vehicle_number
	item.vehicle_model=vehicle_model
	item.current_weight=current.weight
	temp_value=(current_weight - item.vehicle_model.max_weight) / item.vehicle_model.max_weight
	print (temp_value)
	item.vehicle_overweight = temp_value
	print (item.vehicle_overweight)
	item.save()
	
		