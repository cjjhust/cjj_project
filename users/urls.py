from django.conf.urls import url
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
urlpatterns = [
    #登录页面
    path('login/', LoginView.as_view(template_name='login.html'), name="login"),
     #  注销
    url(r'^logout/$', views.logout_view, name='logout'),
     #  注册页面
    url(r'^register/$', views.register, name='register'),
  ]