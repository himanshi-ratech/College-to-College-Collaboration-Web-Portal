from django.shortcuts import render,redirect
from django.http import HttpResponse 
from webstore.models import * 
from django import forms
from django.contrib.auth import authenticate, login,  logout
from django.contrib import messages
from .models import Register
import datetime 
# from store.models import * 
# Create your views here.
def test(request):
    return HttpResponse("<h1>hello world</h1>")
def home(request):
    return HttpResponse("<h1>This is Home Page</h1>")
def splash(request):
    return render(request, 'splash.html')
def home(request):    
    return render(request, 'home.html' )


# def register_view(request):
#     return render(request, 'register.html')
# def registration(request):
#     if request.method=='GET':
#         name1= request.GET['name']
#         email1= request.GET['email']
#         password1= request.GET['password']
#         r=Register(name=name1, email=email1, password=password1)
#         r.save()
#         return render(request, 'register.html', {'message': 'Registration successful!'}) # json
# Create your views here. to start you testing server

def index(request):    
    return render(request, 'index.html' )

def student_register(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        email = request.GET.get('email')     
        password = request.GET.get('password')
        confirm = request.GET.get('confirm')
        

        if name and email and password and confirm:
            if password != confirm:
                return render(request, 'studentsign.html', {'error': 'Passwords do not match'})
            if not email.endswith("@gmail.com"):
                return render(request, 'studentsign.html', {'error': 'Student must use @gmail.com'})
            
            Student.objects.create(name=name, email=email, password=password)
            messages.success(request, "Student Account created successfully! Please log in.")
            return redirect('studentlog')

    return render(request, 'studentsign.html')


def faculty_register(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        email = request.GET.get('email')
        password = request.GET.get('password')
        confirm = request.GET.get('confirm')

        if username and email and password and confirm:
            if password != confirm:
                return render(request, 'signfac.html', {'error': 'Passwords do not match'})
            if not email.endswith("@edu.com"):
                return render(request, 'signfac.html', {'error': 'Faculty must use @edu.com'})
            
            Faculty.objects.create(name=username, email=email, password=password)
            messages.success(request, "Faculty Account created successfully! Please log in.")
            return redirect('facultylog')

    return render(request, 'signfac.html')



def studentlog(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Student.objects.filter(email=email, password=password).first()
        if user:
            return redirect('home')
        else:
            return render(request, 'studentlog.html', {'error': 'Invalid student credentials'})

    return render(request, 'studentlog.html')

def facultylog(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Faculty.objects.filter(email=email, password=password).first()
        if user:
            return redirect('new_home')
        else:
            return render(request, 'facultylog.html', {'error': 'Invalid faculty credentials'})

    return render(request, 'facultylog.html')


def home(request):
    return render(request, 'home.html')

def venue(request):
    return render(request,'venue.html')
def contact(request):
    return render(request,'contact.html')

def query(request):
    if request.method == "POST":
        message = request.POST['message']
        name = request.POST['name']
        email = request.POST['email']
        subject= request.POST['subject']
        u = Query(message=message, name=name, email=email, subject=subject)
        u.save()
        return redirect('contact')

def studentprofile(request):
    return render(request, 'studentprofile.html')

def new_home(request):
    return render(request, 'new_home.html')

def event(request):
    return render (request,'event.html')

def register(request, event_name):
    # Get or create event
    event, created = Event.objects.get_or_create(
        name=event_name,
        defaults={'time': 'TBD', 'university': 'Unknown'}
    )

    if request.method == 'POST':
        Registration.objects.create(
            event=event,
            student_name=request.POST['name'],
            college=request.POST['college'],
            branch=request.POST['branch'],
            roll_no=request.POST['roll_no'],
            department=request.POST['department']
        )
        return redirect('event')

    return render(request, 'register.html', {'event_name': event_name})

#json format- json format in Django and dictionary in python


## for new post
# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.views.decorators.http import require_POST

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("feed")
    else:
        form = PostForm()
    return render(request, "create_post.html", {"form": form})


def feed(request):
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "feed.html", {"posts": posts})

def post(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post.html', {'posts': posts})

@require_POST
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.likes += 1
    post.save()
    return redirect("feed")


@require_POST
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    text = CommentForm(request.POST)

    if text.is_valid():
        # Comment.objects.create(post=post, text=text)
        comment = text.save(commit=False)
        comment.post = post
        comment.save()
    return redirect("feed")


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Student_Detail
from .forms import StudentDetailForm

def studentprofile(request):
    if request.method == 'POST':
        form = StudentDetailForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student profile created successfully!")
            return redirect('studentprofile')
    else:
        form = StudentDetailForm()

    students = Student_Detail.objects.all()
    return render(request, "studentprofile.html", {"form": form, "students": students})


def edit(request, id):
    user = get_object_or_404(Student_Detail, id=id)
    form = StudentDetailForm(instance=user)
    return render(request, "edit.html", {"form": form, "user": user})


def edit_profile(request, id):
    user = get_object_or_404(Student_Detail, id=id)
    if request.method == "POST":
        form = StudentDetailForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Student Information updated successfully!")
            return redirect('studentprofile')
        else:
            return render(request, "edit.html", {"form": form, "error": "Invalid form submission."})
    else:
        return render(request, "edit.html", {"form": StudentDetailForm(instance=user)})

def event_new(request):
    return render (request,'2event.html')

from .models import Event, Registration

def student_registered(request, event_name):
    # Get the event
    event = get_object_or_404(Event, name=event_name)

    # Filter registrations for this event only
    registered_students = Registration.objects.filter(event=event)

    return render(request, 'table.html', {
        'event_name': event_name,
        'registered_students': registered_students
    })
    
def venue_new(request):
    return render (request,'2venue.html')

def contact_new(request):
    return render (request,'2contact.html')