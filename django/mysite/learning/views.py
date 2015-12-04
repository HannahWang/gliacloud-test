from django.shortcuts import render

# Create your views here.
from datetime import datetime
from learning.models import Post
def hello_world(request):
	posts = Post.objects.all()
	return render(request, 'hello_world.html', {
		'posts': posts,
	})
