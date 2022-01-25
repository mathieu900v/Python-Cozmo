from django.urls import path
from . import views

app_name = 'website_cozmo'
urlpatterns = [
    path('', views.index, name='index'),
    path("home", views.home, name='home'),
    path("game", views.game, name='game'),
    path("libre", views.libre, name='libre'),
    path("histoire", views.histoire, name='histoire'),
    path("signout", views.signout, name='signout'),
    path("signup", views.signup, name='signup'),
    path("createprogram", views.createprogram, name='createprogram'),
    path("inscription_page", views.inscription_page, name='inscription_page')

]
