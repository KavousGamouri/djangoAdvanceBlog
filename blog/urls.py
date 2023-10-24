from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/update/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/author/<int:author_id>', views.IndexView.as_view(), name='all_post_author'),
    path('post/category/<str:cat_name>', views.IndexView.as_view(), name='all_post_category'),
    path('contact', views.ContactVIew.as_view(), name='contact'),
    path('search/', views.SearchView.as_view(), name='search'),
]
