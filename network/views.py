from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
import json

from .models import User, Post, Likes, Follow

@login_required(login_url='/login')
def index(request):
    paginator = Paginator(Post.objects.all().order_by('-timestamp'), 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "network/index.html", context={
        
        "page_obj" : page_obj
    })

@login_required(login_url='/login')
def following(request):
    followings_posts = []
    
    for following in request.user.user_followings.all():
        followings_posts = (following.follower.posts.all())
        
    
    paginator = Paginator(followings_posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, "network/following.html", context={
        "page_obj" : page_obj
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def create_post(request):
    if request.method == "POST":
        content = request.POST["post"]
        if not content:
            return HttpResponse("Please Provide Content")
        
        post = Post(creator = request.user, content=content)
        post.save()

        return redirect(reverse("index"))
    
    return redirect(reverse("index"))

def profile(request, user):
    user =  User.objects.filter(username=user).first()
    if not user:
        return HttpResponse("Profile doesn't exist")
    followings = []
    for following in user.user_followers.all():
        followings.append(following.following.username)

    paginator = Paginator(user.posts.all().order_by("-timestamp"), 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "network/profile.html", context={
        "profile_user" : user,
        "followings" : followings,
        "page_obj" : page_obj
        
    })

def follow(request):
    if request.method == "POST":
        user = request.POST["profile_user"]
        action = request.POST["follow"]

        if action == "follow":
            following = Follow(following = request.user, follower = User.objects.get(username=user))
            following.save()

            
        elif action == "unfollow":
            unfollowing = Follow.objects.get(following = request.user, follower = User.objects.get(username=user))
            unfollowing.delete()

        return HttpResponseRedirect(reverse("profile", kwargs={
            "user" : user
        })
        )
    
    return HttpResponseRedirect(reverse("profile", kwargs={
            "user" : user
        })
        )

@csrf_exempt

def edit(request, id):
    if request.method != "POST":
        return HttpResponse("Error")
    id = int(id)
    new_content = json.loads(request.body)
    post = Post.objects.get(id=id)
    post.content = new_content["content"]
    post.save()

    return  JsonResponse({"content": f"{new_content['content']}"}, status=201)
        
@csrf_exempt
def like(request, id):
    if request.method != "POST":
        return HttpResponse("Error")
    id = int(id)
    new_content = json.loads(request.body)
    post = Post.objects.get(id=id)
    creator = User.objects.get(username=new_content["creator"])
    if new_content["like"]:
        post.likes.add(creator)
    else:
        post.likes.remove(creator)
        
    post.save()
    return  JsonResponse({"content": f"Liked Succesfully"}, status=201)