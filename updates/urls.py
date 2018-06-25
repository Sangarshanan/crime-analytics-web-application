from django.conf.urls import url,include
from django.views.generic import ListView, DetailView
from updates.models import Post
from . import views

urlpatterns = [ url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date") [:25],
	template_name = "blog.html")),

				url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Post,
														template_name='post.html')),
				url(r'^port', views.port , name = 'port'),

				url(r'^add', views.add_model , name = 'add_model'),


]
