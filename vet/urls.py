from django.urls import path
from . import views
# from .views import detail
# from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.home, name=''),
    path('contact', views.contact, name="contact"),
    path('addpet', views.addpet, name="addpet"),
    path('login', views.login_request, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout_request, name="logout"),
    path('changepassword', views.change_password, name="change_password"),
    path('editprofile', views.editprofile, name="editprofile"),
]
