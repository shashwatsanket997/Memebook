from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Post, PostLikes
from .forms import PostForm, RegistrationForm
# Create your views here.

# def HelloWorld(request):
#     return render(request, "createPost.html", { 'name': "Shashwat Sanket" })

@login_required(login_url="login")
def getPosts(request):
    print(request.user)
    posts = Post.objects.all() 
    return render(request, "index.html", { 'posts': posts})

@login_required(login_url="login")
def createPost(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("posts")
    else:
        return render(request, 'createPost.html', {'form': PostForm()})

@login_required(login_url="login")
def editPost(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.author != request.user:
        #send a message for forbidden
        redirect("home")  
    form = PostForm(request.POST or None, instance=post)
    if request.method == "POST" and form.is_valid():
        form.save()
        #message
        return redirect("home")
    return render(request, "createPost.html", { 'form': form })
    
@login_required(login_url="login")
def deletePost(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    if post.author != request.user:
        #send a message for forbidden
        return redirect("home")
    post.delete()
    #set message
    return redirect("home")

@login_required(login_url="login")
def likePost(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    user = request.user
    checkIfLiked = PostLikes.objects.filter(post=post, user=user)
    if checkIfLiked.exists():
        checkIfLiked.delete()
    else:
        like = PostLikes(post = post, user = user)
        like.save()
    return redirect("home")

        
@login_required(login_url="login")
def getPost(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "postDetail.html", { 'post': post})

def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form =RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    return render(request, "register.html", { "form": form})


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if username=="" or password=="" is None:
            return render(request, "login.html", { "error_message": "Username and Password are required"})
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect("home")
            else:
                return render(request, 'login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'login.html', {'error_message': 'Invalid login'})
    return render(request, "login.html")


def logout(request):
    auth_logout(request)
    return redirect("login")