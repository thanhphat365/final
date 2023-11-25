from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post, Comment
import requests
from django.contrib.auth import authenticate, login,logout
from .forms import LoginForm,RegistrationForm
from django.contrib.auth.models import User
from .models import Blog
from .forms import BlogForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
#logout
def user_logout(request):
    logout(request)
    return redirect('home')
#detail_template
def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.all()
    # if comment_model.exists():
    return render(request, 'posts/detail.html', {'post':post,'comments':comments} )

    # return render(request, 'posts/detail.html', {'post':post})
# Create your views here.
def home(request):
    api_key = 'b7f9eaed03ddc480483400afbeaf5baa'
    url = 'http://api.mediastack.com/v1/news'
    params = {
        'access_key': api_key,
        'limit': 100,
        'categories': 'general',
    }
    response = requests.get(url, params=params)
    data = response.json().get('data')  # Use get() method to retrieve 'data' with a default value of None
    
    if data:
        for news in data:
            if news['image']:

                check = Post.objects.filter(title=news['title'])
                if check:
                    # do something with
                    pass
                else:
                    post = Post(category = news['category'], title = news['title'],author = news['author'],image = news['image'],description = news['description'])
                    post.save()
        home_posts = Post.objects.filter(category = 'general')
        

            
        return render(request, 'pages/home.html', {'home_posts': home_posts})
    data = {
        "test":'test'
    }
    return render(request, 'pages/home.html',{"data":data})
#Sport
def sport(request):
    api_key = 'b7f9eaed03ddc480483400afbeaf5baa'
    url = 'http://api.mediastack.com/v1/news'
    params = {
        'access_key': api_key,
        'limit': 100,
        'categories': 'sports',
    }
    response = requests.get(url, params=params)
    data = response.json().get('data')  # Use get() method to retrieve 'data' with a default value of None
    
    if data:
        for news in data:
            if news['image']:

                check = Post.objects.filter(title=news['title'])
                if check:
                    # do something with
                    pass
                else:
                    post = Post(category = news['category'], title = news['title'],author = news['author'],image = news['image'],description = news['description'])
                    post.save()
        sports_posts = Post.objects.filter(category = 'sports')
        return render(request, 'pages/sport.html', {'sports_posts': sports_posts})
    data = {
        "test":'test'
    }
    return render(request, 'pages/sport.html',{"data":data})


def technology(request):
    api_key = 'b7f9eaed03ddc480483400afbeaf5baa'
    url = 'http://api.mediastack.com/v1/news'
    params = {
        'access_key': api_key,
        'limit': 100,
        'categories': 'technology',
    }
    response = requests.get(url, params=params)
    data = response.json().get('data')  # Use get() method to retrieve 'data' with a default value of None
    
    if data:
        for news in data:
            if news['image']:

                check = Post.objects.filter(title=news['title'])
                if check:
                    # do something with
                    pass
                else:
                    post = Post(category = news['category'], title = news['title'],author = news['author'],image = news['image'],description = news['description'])
                    post.save()
        technologies_posts = Post.objects.filter(category = 'technology')
        return render(request, 'pages/technology.html', {'technologies_posts': technologies_posts})
    data = {
        "test":'test'
    }
    return render(request, 'pages/technology.html',{"data":data})

def health(request):
    api_key = 'b7f9eaed03ddc480483400afbeaf5baa'
    url = 'http://api.mediastack.com/v1/news'
    params = {
        'access_key': api_key,
        'limit': 100,
        'categories': 'health',
    }
    response = requests.get(url, params=params)
    data = response.json().get('data')  # Use get() method to retrieve 'data' with a default value of None
    
    if data:
        for news in data:
            if news['image']:

                check = Post.objects.filter(title=news['title'])
                if check:
                    # do something with
                    pass
                else:
                    post = Post(category = news['category'], title = news['title'],author = news['author'],image = news['image'],description = news['description'])
                    post.save()
        health_posts = Post.objects.filter(category = 'health')
        return render(request, 'pages/health.html', {'health_posts': health_posts})
    data = {
        "test":'test'
    }
    return render(request, 'pages/health.html',{"data":data})


#business
def business(request):
    api_key = 'b7f9eaed03ddc480483400afbeaf5baa'
    url = 'http://api.mediastack.com/v1/news'
    params = {
        'access_key': api_key,
        'limit': 100,
        'categories': 'business',
    }
    response = requests.get(url, params=params)
    data = response.json().get('data')  # Use get() method to retrieve 'data' with a default value of None
    
    if data:
        for news in data:
            if news['image']:

                check = Post.objects.filter(title=news['title'])
                if check:
                    # do something with
                    pass
                else:
                    post = Post(category = news['category'], title = news['title'],author = news['author'],image = news['image'],description = news['description'])
                    post.save()
        business_posts = Post.objects.filter(category = 'business')
        return render(request, 'pages/business.html', {'business_posts': business_posts})
    data = {
        "test":'test'
    }
    return render(request, 'pages/business.html',{"data":data})

#entertainment
def entertainment(request):
    api_key = 'b7f9eaed03ddc480483400afbeaf5baa'
    url = 'http://api.mediastack.com/v1/news'
    params = {
        'access_key': api_key,
        'limit': 100,
        'categories': 'entertainment',
    }
    response = requests.get(url, params=params)
    data = response.json().get('data')  # Use get() method to retrieve 'data' with a default value of None
    
    if data:
        for news in data:
            if news['image']:

                check = Post.objects.filter(title=news['title'])
                if check:
                    # do something with
                    pass
                else:
                    post = Post(category = news['category'], title = news['title'],author = news['author'],image = news['image'],description = news['description'])
                    post.save()
        entertainment_posts = Post.objects.filter(category = 'entertainment')
        return render(request, 'pages/entertainment.html', {'entertainment_posts': entertainment_posts})
    data = {
        "test":'test'
    }
    return render(request, 'pages/entertaintment.html',{"data":data})

#science
def science(request):
    api_key = 'b7f9eaed03ddc480483400afbeaf5baa'
    url = 'http://api.mediastack.com/v1/news'
    params = {
        'access_key': api_key,
        'limit': 100,
        'categories': 'science',
    }
    response = requests.get(url, params=params)
    data = response.json().get('data')  # Use get() method to retrieve 'data' with a default value of None
    
    if data:
        for news in data:
            if news['image']:

                check = Post.objects.filter(title=news['title'])
                if check:
                    # do something with
                    pass
                else:
                    post = Post(category = news['category'], title = news['title'],author = news['author'],image = news['image'],description = news['description'])
                    post.save()
        science_posts = Post.objects.filter(category = 'science')
        return render(request, 'pages/science.html', {'science_posts': science_posts})
    data = {
        "test":'test'
    }
    return render(request, 'pages/science.html',{"data":data})

#register
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'posts/register.html', {'form': form})
#login
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error('password', 'Incorrect password.')
    else:
        form = LoginForm()
    return render(request, 'posts/login.html', {'form': form})

#crete_Blog
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = BlogForm()
    return render(request, 'posts/create_blog.html', {'form': form})
#about
def about(request):
    return render(request,"pages/about.html",)
#comment
def comment_view(request,post_id,author):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        user_comment= request.POST['user_comment']  
        comment_model=Comment(user=author,comment=user_comment,post= post)
        comment_model.save()
        return redirect( 'detail',post_id=post_id)
    