from django.db import models



class TipperModel(models.Model):
	model_name = models.CharField(max_length=20)
	max_weight = models.FloatField()


  

class Vehicle(models.Model):
	number = models.CharField(max_length=10)
	model = models.ForeignKey(TipperModel)
	current_weight = models.FloatField()
	
	

	
		