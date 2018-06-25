
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserChangeForm


# Create your views here.
def port(request):
	template = loader.get_template('pst.html')
	return HttpResponse(template.render())


from django import forms
from django.utils import timezone
from updates.forms import Postform
def add_model(request):
 
    if request.method == "POST":
        form = Postform(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/updates')
 
    else:
 
        form = Postform()
 
        return render(request, "add.html", {'form': form})
