from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Post, Comment
from datetime import datetime

# Create your views here.


def index(request):
    posts = Post.objects.all()
    return render(request, "index.html", {"posts": posts})

def post(request, id):

    if Post.objects.filter(id=id).exists():
        post = Post.objects.get(id=id)
        comments = Comment.objects.all()
        current_post = str(post.id)
        return render(request, "post.html", {"post":post, "comments":comments, "current_post":current_post})
    else:
        return render(request, "notFound.html")


def login(request):

    if request.method=="POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid credentials.")
            return redirect("login")
    else:
        return render(request, "login.html")

def register(request):

    if request.method=="POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        cnfpassword = request.POST["cnfpassword"]

        if password==cnfpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists.")
                return redirect("register")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "User Name already exists.")
                return redirect("register")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect("login")
        else:
            messages.info(request, "Both passwords should match.")
            return redirect("register")
    else:
        return render(request, "register.html")

    return render(request, "register.html")

def logout(request):
    auth.logout(request)
    return redirect("/")

def compose(request):
    if request.method=="POST":
        title = request.POST["title"]
        content = request.POST["content"]
        author = request.POST["author"]
        created_at = str(datetime.now)

        newPost = Post(title=title, content=content, author=author)
        newPost.save()
        return redirect("/")
    return render(request, "compose.html")

def addComment(request):
    if request.method=="POST":
        comment_by = request.POST["comment_by"]
        post = request.POST["post"]
        comment = request.POST["comment"]

        newComment = Comment(comment_by=comment_by, post=post, comment=comment)
        newComment.save()
        return redirect("post/"+post)

# def page_not_found_view(request, exception):
#     return render(request, "notFound.html", status=404)