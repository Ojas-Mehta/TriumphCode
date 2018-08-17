from django.contrib import admin
from django.conf.urls import include, url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   url(r'^$', views.home, name='home'),
   url(r'^register/login/$', auth_views.login,{'template_name': 'register/login.html'}, name='login'),
   #url(r'^register/signup/$', views.signuppage, name='signup'),
   url(r'^register/signup/$', views.signup, name='signup'),
   url(r'^dashboard/logout/$', auth_views.logout, {'next_page':'/'}, name='logout'),
   url(r'dashboard/CompileAndRun/$', views.editor, name='editor'),
   url(r'dashboard/CompileAndRun/submit', views.submit, name='submit'),

]
