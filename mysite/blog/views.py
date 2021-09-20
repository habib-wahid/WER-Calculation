from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
# Create your views here.

posts = [
    {
        'given_text':'আমি ভাত খাই',
        'automated_text':'আমি ভাত খাই না'
    },
    {
        'given_text':'আমি স্কুলে যাই',
        'automated_text':'আমি স্কুলে যাই না'
    },
    {
        'given_text':"তুমি একটি বলদ",
        'automated_text':'ছাগল একটা'
    }
]


def home(request):
    form = PostForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('blog-calculation')

    return render(request,'blog/home.html',{'form':form})

def calculation(request):
    context = {
        'post': Post.objects.all().last()
    }
    return render(request,'blog/calculation.html',context)