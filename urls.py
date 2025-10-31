"""
URL configuration for web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webstore import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.test, name="test"),
    path('home/', views.home, name="home"),
    path('home/home/', views.home, name="home"),
    # path('splash/', views.splash, name="splash"),    
    # path('register/', views.register_view, name='register_view'),
    # path('registration/', views.registration, name='registration'),
    # path('signup/', views.signup, name='signup'),    
    # path('login/', views.login, name='login'),  # Handles both GET and POST
    path('index/', views.index, name='index'),

    # Student URLs
    path('student/register/', views.student_register, name='student_register'),
    path('student/login/', views.studentlog, name='studentlog'),

    # Faculty URLs
    path('faculty/register/', views.faculty_register, name='faculty_register'),
    path('faculty/login/', views.facultylog, name='facultylog'),
    
    path('signfac/', views.faculty_register, name="signfac"),    
    path('studentsign/', views.student_register, name="studentsign"),    
    path('studentlog/', views.studentlog, name="studentlog"),    
    path('facultylog/', views.facultylog, name="facultylog"),    
    # Admin login (if you add later)
    # path('admin/login/', views.adminlog, name='logadmin'),
    
    path('venue/', views.venue, name='venue'),
    path('venue/venue/', views.venue, name='venue'),
    path('contact/', views.contact, name='contact'),       
    path('query/', views.query, name='query'),
    path('studentprofile/', views.studentprofile, name='studentprofile'),
    path('event/', views.event, name='event'),
    path('register/<str:event_name>/', views.register, name='register'),
    
    
    #new for posts
    path('create/', views.create_post, name='create_post'),
    path("feed/", views.feed, name="feed"),   # 👈 feed page
    path("like/<int:post_id>/", views.like_post, name="like_post"),
    path("comment/<int:post_id>/", views.add_comment, name="add_comment"),   
    
    path('studentprofile/', views.studentprofile, name='studentprofile'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('edit_profile/<int:id>/', views.edit_profile, name='edit_profile'),
    
    path('new_home/', views.new_home, name="new_home"),    
    path('post/', views.post, name="post"),    
    path('2event/', views.event_new, name="2event"),    
    path('registered/<str:event_name>/', views.student_registered, name='student_registered'),
    path('2venue/', views.venue_new, name="2venue"),    
    path('2contact/', views.contact_new, name="2contact"),    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])