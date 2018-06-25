from django.contrib import admin

# Register your models here.
from app.models import crimes_against_women
from app.models import murder

admin.site.register(crimes_against_women)

admin.site.register(murder)