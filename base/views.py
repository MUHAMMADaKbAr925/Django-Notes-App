from django.shortcuts import render, redirect
from . models import Message
from django.contrib import messages
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    
    if request.user.is_authenticated:
        user = request.user
        messages = Message.objects.filter(user=user)
    else:
        messages = []
        return redirect('login')
    context = {'messages' : messages}



    return render(request, 'base/new_home.html', context)

@login_required
def note_view(request, pk):
    message = Message.objects.get(id=pk)
    if request.method == 'POST':
        new_body = request.POST.get('body1')
        new_title = request.POST.get('title')
        if new_body and new_title:     
            message.title = new_title

            message.body = new_body
            message.save()
            messages.success(request, 'Message updated successfully')
            return redirect('home')  # Redirect to the same page or another view
        else:
            messages.error(request, 'Message body cannot be empty')

    context = {'message':message}

    return render(request, 'base/note.html', context)

def register_view(request):
    page = 'register'
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserForm()
    
    return render(request, 'base/login_register_new.html', {'form':form, 'page':page})

def loginPage(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, "Username or password is not existant")
    context = {'page':page}
    return render(request,'base/login_register_new.html',context)



def newMessage(request):

    if request.method == 'POST':
         
         message, created = Message.objects.get_or_create(
             user = request.user,
             title = request.POST.get('title'),
             body = request.POST.get('body')

         )
         message.save()
         return redirect('home')

    return render(request, 'base/new_new.html')


def deleteMessage(request, pk):

    if request.method == 'POST':
        id = pk
        message = Message.objects.get(id=pk)
        message.delete()
        return redirect('home')


    return render(request, 'base/delete.html')


def logoutPage(request):
    logout(request)
    return redirect('login')