from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('',login_required(views.home,login_url='/user/login/?next=/user/login/'),name='home'),
]