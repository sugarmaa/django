from django.shortcuts import render
from BlogApp.models import Blog
from BlogApp.models import Chart

def getAllBlogs(request):
    blogs = Blog.objects.all()
    iTCategoryCount = Blog.objects.filter(category = 'IT').count()
    foodCategoryCount = Blog.objects.filter(category = 'Food').count()
    return render(request, 'blogs.html', {'htmlBlogs': blogs, 'itCount': iTCategoryCount, 'foodCount': foodCategoryCount})

def getAllItCategoryBlogs(request):
    blogs = Blog.objects.filter(category = 'IT')
    iTCategoryCount = Blog.objects.filter(category = 'IT').count()    
    foodCategoryCount = Blog.objects.filter(category = 'Food').count()
    return render(request, 'blogs.html', {'htmlBlogs': blogs, 'itCount': iTCategoryCount, 'foodCount': foodCategoryCount})

def getAllFoodCategoryBlogs(request):
    blogs = Blog.objects.filter(category = 'Food')
    iTCategoryCount = Blog.objects.filter(category = 'IT').count()    
    foodCategoryCount = Blog.objects.filter(category = 'Food').count()
    return render(request, 'blogs.html', {'htmlBlogs': blogs, 'itCount': iTCategoryCount, 'foodCount': foodCategoryCount})

def getSelectedBlog(request, blogId):
    blog = Blog.objects.get(id = blogId)
    return render(request, 'blog.html', {'selectedBlog': blog})

def hooson(request, exc):
    return render(request, '404.html', {})

def aldaa(request):
    return render(request, '500.html', {})

def chart(request):
    chart = Chart.objects.all().first()
    a = [chart.Monday, chart.Tuesday, chart.Wednesday, chart.Thursday, chart.Friday,  chart.Saturday, chart.Sunday]
    return render(request, 'index.html', {'chartValues': a})