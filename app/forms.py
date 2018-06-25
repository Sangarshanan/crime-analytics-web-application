from django.forms import ModelForm
from app.models import crimes_against_women
from app.models import murder
from app.models import murder
from app.models import sanfran
from django import forms  



class caw(ModelForm):
	class Meta:
		model = crimes_against_women
		fields = ['Area_Name','Year','Subgroup','Rape_Cases_Reported','Victims_Above_50_Yrs','Victims_Between_10to14_Yrs','Victims_Between_14to18_Yrs','Victims_Between_18to30_Yrs','Victims_Between_30to50_Yrs','Victims_of_Rape_Total','Victims_Upto_10_Yrs']



class mv(ModelForm):
	class Meta:
		model = murder
		fields = ['Area_Name','Year','Group_Name','Victims_Above_50_Yrs','Victims_Total','Victims_Upto_10_15_Yrs','Victims_Upto_10_Yrs','Victims_Upto_15_18_Yrs','Victims_Upto_18_30_Yrs','Victims_Upto_30_50_Yrs']

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

class sf(ModelForm):
	Day = forms.ChoiceField(choices=DAYS, required=True )
	location = forms.ChoiceField(choices=LOCATIONS, required=True )

	class Meta:
		model = sanfran
		fields = ['Day','location']