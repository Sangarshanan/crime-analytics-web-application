import csv,sys,os

project_dir = "C:/Users/Sangarshanan Veera/Desktop/Hack/DJANGO/crime analytics"

#Добавляем в переменную sys.path путь до проекта Django
sys.path.append(project_dir)

#Определяем переменную с настройками Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'practiceapp.settings'

#Импортируем модуль Django
import django

#Загружаем настройки Django
django.setup()
#Импортируем модель Post
from app.models import murder

#Считываем CSV-файл
data = csv.reader(open("C:/Users/Sangarshanan Veera/Desktop/Hack/DJANGO/crime analytics/32_Murder_victim_ag_sex.csv"),delimiter=',')
for row in data:
	if row[0] != 'Area_Name':

		post = murder()
		post.Area_Name = row[0]
		post.Year = row[1]
		post.Group_Name = row[2]
		post.Victims_Total = row[5]
		post.Victims_Above_50_Yrs = row[4]
		post.Victims_Upto_10_15_Yrs = row[6]
		post.Victims_Upto_10_Yrs = row[7]
		post.Victims_Upto_15_18_Yrs = row[8]
		post.Victims_Upto_18_30_Yrs = row[9]
		post.Victims_Upto_30_50_Yrs = row[10]
		post.save()
