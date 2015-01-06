from django.shortcuts import get_object_or_404, render
from blog.models import Post
from django.views import generic


class IndexView(generic.ListView):
	template_name = 'blog/index.html'
	# context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last five published quesitons"""
		return Post.objects.order_by('-created')[:5]

	# def index(request):
	# 	posts = Post.objects.filter(published=True)
	# 	return render(request, 'blog/index.html', {'posts':posts})

def post(request, slug):
	post = get_object_or_404(Post, slug=slug)
	return render(request, 'blog/post.html', {'post':post})