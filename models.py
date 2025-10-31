from django.db import models
# from webstore.forms import *
from django.contrib.auth.models import User
from django.contrib import messages
# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=50)
    class Meta:
        db_table = 'register'
        
class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    class Meta:
        db_table= 'student'
        
class Faculty(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    class Meta:
        db_table= 'faculty'
        
class Query(models.Model):
    message=models.CharField(max_length=200)
    name= models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=100)
    class Meta:
        db_table= 'query'


class userprofile (models.Model):
     username=models.CharField(max_length=50)
     password=models.CharField(max_length=50)
     email=models.EmailField()
     class Meta:
         db_table= 'userprofile'


class Event(models.Model):
    name = models.CharField(max_length=100)
    time = models.CharField(max_length=50)
    university = models.CharField(max_length=100)
    # add more event-specific info if needed

    def __str__(self):
        return self.name

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=100, blank=True)  # new
    student_name = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    branch = models.CharField(max_length=50)
    roll_no = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    paid = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        self.event_name = self.event.name  # auto-fill
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student_name} - {self.event.name}"


# new for post

# models.py

class Post(models.Model):
    # remove dependency on Django's User
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100, default="Anonymous")  # 👈 replaces user
    caption = models.TextField()
    image = models.ImageField(upload_to="static/Posts/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)  # simpler like count

    def total_likes(self):
        return self.likes

    def __str__(self):
        return f"{self.author_name} - {self.caption[:20]}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author_name = models.CharField(max_length=100, default="Anonymous")
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author_name} on {self.post.id}"
    def total_comments(self):
        return self.comments.count()

class Student_Detail(models.Model):
    name=models.CharField(max_length=100)
    roll=models.CharField(max_length=100)
    branch=models.CharField(max_length=100)
    year=models.CharField(max_length=100)
    dept=models.CharField(max_length=100)
    email=models.EmailField()
    contact=models.CharField(max_length=100)
    
    class Meta:
        db_table = 'Student_Detail'