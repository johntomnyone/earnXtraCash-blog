from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
from .forms import CommentForm

# Create your views here.

class PostList(generic.ListView):
	queryset = Post.objects.filter(status=1).order_by('-created_on')
	template_name = 'index.html'
	paginate_by = 3
	


def post_detail(request, slug):
	#model = Post
	queryset = Post.objects.filter(status=1).order_by('-created_on')
	if queryset.exists():
		post_item = queryset.all()
	template_name = 'post_detail.html'
	post = get_object_or_404(Post, slug=slug)
	comments = post.comments.filter(active=True)
	new_comment = None
	# Comment posted
	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():

			# Create Comment object but don't save to database
			new_comment = comment_form.save(commit=False)
			# Assign the current post to the comment
			new_comment.post = post
			# Save the comment to the database
			new_comment.save()
	else:
		comment_form = CommentForm()

	return render(request, template_name, {'post_item':post_item, 'post': post, 'comments': comments, 'new_comment': new_comment, 'comment_form': comment_form})


def freelancing(request):
	queryset = Post.objects.filter(status=0).order_by('-created_on')
	if queryset.exists():
		posts = queryset.all()
	mypost = Post.objects.filter(status=1).order_by('-created_on')
	if mypost.exists():
		mypost_item = mypost.all()
	return render(request, 'freelancing.html', {'posts':posts, 'mypost_item':mypost_item})