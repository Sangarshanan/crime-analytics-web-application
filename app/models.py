from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class crimes_against_women(models.Model):
	Area_Name = models.CharField(max_length=140)
	Year = models.CharField(max_length=140)
	Subgroup = models.CharField(max_length=140)
	Rape_Cases_Reported = models.CharField(max_length=10,null=True)
	Victims_Above_50_Yrs = models.CharField(max_length=10,null=True)
	Victims_Between_10to14_Yrs= models.CharField(max_length=10,null=True)
	Victims_Between_14to18_Yrs =models.CharField(max_length=10,null=True)
	Victims_Between_18to30_Yrs = models.CharField(max_length=10,null=True)
	Victims_Between_30to50_Yrs = models.CharField(max_length=10,null=True)
	Victims_of_Rape_Total =models.CharField(max_length=10,null=True)
	Victims_Upto_10_Yrs = models.CharField(max_length=10,null=True)

	def __str__(self):
		return self.Area_Name

class murder(models.Model):
	Area_Name = models.CharField(max_length=140)
	Year = models.CharField(max_length=140)
	Group_Name = models.CharField(max_length=140)
	Victims_Above_50_Yrs = models.CharField(max_length=10,null=True)
	Victims_Total = models.CharField(max_length=10,null=True)
	Victims_Upto_10_15_Yrs=models.CharField(max_length=10,null=True)
	Victims_Upto_10_Yrs = models.CharField(max_length=10,null=True)
	Victims_Upto_15_18_Yrs = models.CharField(max_length=10,null=True)
	Victims_Upto_18_30_Yrs = models.CharField(max_length=10,null=True)
	Victims_Upto_30_50_Yrs = models.CharField(max_length=10,null=True)

	def __str__(self):
		return self.Area_Name


DAYS = (  
    ('Sunday', 'Sunday'),
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),


)
LOCATIONS = (  
    ('BAYVIEW', 'BAYVIEW'),
    ('CENTRAL', 'CENTRAL'),
    ('INGLESIDE', 'INGLESIDE'),
    ('MISSION', 'MISSION'),
    ('NORTHERN', 'NORTHERN'),
    ('PARK', 'PARK'),
    ('RICHMOND', 'RICHMOND'),
    ('SOUTHERN', 'SOUTHERN'),
    ('TARAVAL', 'TARAVAL'),
    ('TENDERLOIN', 'TENDERLOIN'),

)

class sanfran(models.Model):  
    Day         = models.CharField(max_length=10, choices=DAYS)
    Location    = models.CharField(max_length=20, choices=LOCATIONS)
