from django.shortcuts import render, redirect

from django.views import generic

from .forms import CommentForm

from .models import Post


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = "blog/blog.html"

class PostDetail(generic.DetailView):
    model = Post
    template_name = "blog/post_detail.html"

def front_page(request): 
    posts = Post.objects.all()

    return render(request, 'blog/front_page.html', {'posts': posts})

def post_detail(request, slug): 
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

        return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()


    return render(request, 'blog/post_detail.html', {'post': post, 'form': form})