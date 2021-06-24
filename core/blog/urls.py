from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:post>/', views.post, name='post'),
    path('category/<category>', views.CatListView.as_view(), name='category'),
]
