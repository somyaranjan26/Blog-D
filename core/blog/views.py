from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic import ListView
from .forms import NewCommentForm
from .models import Category, Post

def home(request):
    all_posts = Post.newManager.all()
    data = { 'posts' : all_posts }

    return render(request, 'index.html', data)

def post(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    comments = post.comments.filter(status=True)
    user_comment = None

    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False) # not commiting post to db
            user_comment.post = post                       # getting the post details
            user_comment.save()                            # then saving it to db
            return HttpResponseRedirect('/' + post.slug)

    else:
        comment_form = NewCommentForm()

    data = { 'post': post, 
             'comments': comments, 
             'comment': user_comment, 
             'comment_form': comment_form
            }

    return render(request, 'post.html', data)

class CatListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist' # for accessing data in html page

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name = self.kwargs['category']).filter(status='published')
        }
        return content

def category_list(request):
    category_list = Category.objects.exclude(name='default')
    context = {
        "category_list" : category_list, 
    }
    return context