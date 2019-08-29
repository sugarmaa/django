from django.urls import path
from BlogApp import views

urlpatterns = [
    path('chart', views.chart),
    path('', views.getAllBlogs),
    path('it', views.getAllItCategoryBlogs),
    path('food', views.getAllFoodCategoryBlogs),
    path('blog/<blogId>', views.getSelectedBlog),
]