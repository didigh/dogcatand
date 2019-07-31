from django.shortcuts import render, redirect, get_object_or_404 
from django.utils import timezone 
from .models import Blog

# Create your views here.
def start(request):
    return render(request, 'start.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def professional(request):
    blog = Blog.objects.all()
    return render(request, 'professional.html', {'blog':blog})

def detail(request, blog_id):
    blog = Blog.objects.get(pk = blog_id)
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(request, 'detail.html', {'blog' : blog })

def new(request):
    if request.method == 'POST':
        blog = Blog()
        blog.title = request.POST['title']
        # blog.title = request.POST('title', '')
        blog.body = request.POST['body']
        blog.date = timezone.datetime.now()
        blog.save()

        return redirect('professional')
    else:
        return render(request, 'new.html')

def edit(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.save()
        return redirect('professional')
    else:
        return render(request, 'edit.html', {'blog':blog})

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.delete()
    return redirect('professional')