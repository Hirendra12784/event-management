from django.db import models

class eventadd(models.Model):
	edate=models.DateField()
	ename=models.CharField(max_length=70)
	etype=models.CharField(max_length=70)
