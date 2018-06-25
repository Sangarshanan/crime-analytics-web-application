from django.forms import ModelForm
from updates.models import Post

class Postform(ModelForm):
	class Meta:
		model = Post
		fields = ['title','body','date']

