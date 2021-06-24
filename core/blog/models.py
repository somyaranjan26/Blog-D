from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey

class Category(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

def user_directory_path(instance, filename):
    return 'posts/{0}/{1}'.format(instance.title, filename)


class Post(models.Model):

    class NewManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status = 'published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug =  models.SlugField(max_length=250, unique_for_date='publish')
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1, related_name='blog_category')
    content = models.TextField()
    image = models.ImageField(upload_to=user_directory_path, default='posts/default.jpg')
    status = models.CharField(max_length=10, choices=options, default='published')

    objects = models.Manager() # default manager
    newManager = NewManager() # custom manager to show published blogs only

    def get_absolute_url(self):
        return reverse('blog:post', args=[self.slug])

    class Meta:
        ordering = ('-publish',)

    def __str__(self) -> str:
        return self.title


class Comment(MPTTModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    name = models.CharField(max_length=50)
    email = models.EmailField()
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ["publish"]

    def __str__(self) -> str:
        return f"Comment by {self.name}"