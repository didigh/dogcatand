from django.shortcuts import render, redirect, get_object_or_404 
from django.utils import timezone 
from .models import Blog,Comment,Re
from .forms import BlogForm,CommentForm,ReForm

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



def comment_create(request,blog_id):
        if request.method=='POST':
                blog=get_object_or_404(Blog,pk=blog_id)
                form=CommentForm(request.POST)
                if form.is_valid():
                        comment=form.save(commit=False)
                        comment.blog=blog
                        comment.save()
                        return redirect('/'+str(blog.id))
        else:
                form=CommentForm()
                return render(request,'detail.html',{'form':form})

def comment_delete(request, blog_id, comment_id):
        blog = get_object_or_404(Blog, pk = blog_id)
        comment = get_object_or_404(Comment, pk = comment_id)
        comment.delete()
        return redirect('/' + str(blog.id))


def replay_create(request,blog_id,comment_id):        
        if request.method=='POST':
                blog=get_object_or_404(Blog,pk=blog_id)
                comments=get_object_or_404(Comment,pk=comment_id)
                form=ReForm(request.POST)
                if form.is_valid():
                        re=form.save(commit=False)
                        re.comment=comments
                        re.save()
                        return redirect('/'+str(blog.id))
        else:
                form=ReForm()
                return render(request,'detail.html',{'form':form, 'comment': comment})

def replay_delete(request,blog_id,comment_id,re_id):
        blog=get_object_or_404(Blog,pk=blog_id)
        comment=get_object_or_404(Comment,pk=comment_id)
        re=Re.objects.get(pk = re_id)
        re.delete()
        return redirect('/'+str(blog.id))


