from django.shortcuts import render, redirect
from django.http  import HttpResponseRedirect
import datetime as dt
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import MyUser,Neighbor,Post,Business
from .forms import CreateProfileForm, PostForm
# Create your views here.

def welcome(request):
    current_user = request.user
    profile = MyUser.get_user()
    post = Post.get_post()
    return render(request,'index.html',{"current_user":current_user,
                                        "profile":profile,
                                        "post":post})



# def home(request):
#     return render(request, 'home.html')

@login_required(login_url='/accounts/login/')
def neighbor(request):
    date = dt.date.today()
    neighbor = Neighbor.objects.all()


    return render(request, 'hood.html', {"date": date,"neighbor":neighbor,})

def new_neighbor(request):
    current_user = request.user
    form = NewNeihborForm()
    if request.method == 'post':
        form = NewNeighborForm(request.POST, request.FILES)
        if form.is_valid():
            neighbor = form.save(commit=False)
            neighbor.user = current_user
        else:
            if request.method == 'POST':
                form = myNewProfile(request.post,request.FILES)
                neighbor.user = current_user
                neighbor.save()
            return redirect('home')
        return render(request, 'hood.html', {'form':form })


@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    # if current_user.is_authenticated():
    #     return HttpResponseRedirect('current_user')
    if request.method == 'POST':
        form = CreateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.user = current_user
            new.save()
            return redirect(view_profile)
    else:
        form = CreateProfileForm()
    return render(request, 'profile/create_new.html', {"upload_form":form})


@login_required(login_url='/accounts/login/')
def view_neighbor(request):
    current_user = request.user
    myuser = MyUser.get_user()
    posts = Post.get_post()
    count = 0
    jirani= Neighbor.get_neighbor()
    neighbor_2 = get_object_or_404(Neighbor)
    for neighbor_2 in neighbor:
        for user in myuser:
            if user.neighbor.id == neighbor_2.id:
                count += 1
    jirani.occupants_count = count
    jirani.save()
    return redirect('view_neighbor')


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    myuser = MyUser.get_user()
    print(myuser)
    post_form = PostForm()
    for user in myuser:
        if user.user.id == current_user.id:
            # if current_user.is_authenticated():
            #     return HttpResponseRedirect('current_user')
            if request.method == 'POST':
                post_form = PostForm(request.POST,request.FILES)
                if post_form.is_valid():
                    post = post_form.save(commit=False)
                    post.editor = user
                    post.save()
                    return redirect(index)
            else:
                post_form = PostForm()
        return render(request,'post.html',{"post_form":post_form})



@login_required(login_url='/accounts/login/')
def business(request):
    current_user = request.user
    business = Business.get_business()
    return render(request,'biz.html',{"current_user":current_user,
                                           "business":business})

@login_required(login_url='/accounts/login/')
def search_results(request):
    current_user = request.user
    profile = MyUser.get_user()

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_name = Business.find_business(search_term)
        message = f"{search_term}"
        return render(request,'search.html',{"message":message,"business":searched_business})

    else:
        message = 'You havent searched for any term'
    return render(request,'search.html',{"message",message})

@login_required(login_url='/accounts/login/')
def view_neighbor(request):
    current_user = request.user
    myuser = MyUser.get_user()
    post= Post.get_post()
    jirani= Neighbor.get_neighbor()
    return render(request,'hood.html',{"jirani":neighbor,
                                       "post":post,
                                       "myuser":myuser,
                                       "current_user":current_user})
#
# @login_required(login_url='/accounts/login/')
# def profile(request):
#     current_user = request.user
#     profile = MyUser.get_user()
#     posts = Post.get_post()
#     return render(request,'profile/profile.html',{"profile":profile,
#                                                   "current_user":current_user,
#                                                   "posts":posts})


@login_required(login_url='/accounts/login/')
def business(request):
    current_user = request.user
    business = Business.get_business()
    return render(request,'biz.html',{"current_user":current_user,
                                           "business":business})




@login_required(login_url='/accounts/login/')
def view_profile(request):
    current_user = request.user
    profile = MyUser.get_user()
    post = Post.get_post()
    return render(request,'profile/profile.html',{"profile":profile,
                                                  "current_user":current_user,
                                                  "post":post})
