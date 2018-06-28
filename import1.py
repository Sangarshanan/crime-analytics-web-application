import csv,sys,os
os.environ['DJANGO_SETTINGS_MODULE'] = 'practiceapp.settings'
import django
django.setup()
from app.models import crimes_against_women
data = csv.reader(open("20_Victims_of_rape.csv"),delimiter=',')
for row in data:
	if row[0] != 'Area_Name':

		post = crimes_against_women()
		post.Area_Name = row[0]
		post.Year = row[1]
		post.Subgroup = row[2]
		post.Rape_Cases_Reported = row[3]
		post.Victims_Above_50_Yrs = row[4]
		post.Victims_Between_10to14_Yrs = row[5]
		post.Victims_Between_14to18_Yrs = row[6]
		post.Victims_Between_18to30_Yrs = row[7]
		post.Victims_Between_30to50_Yrs = row[8]
		post.Victims_Between_30to50_Yrs = row[9]
		post.Victims_Upto_10_Yrs = row[10]
		post.save()
