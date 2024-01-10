
from django.urls import path
from app_dice_roll import views


urlpatterns = [
    path('', views.home, name='home'),

    path('result/', views.result, name='dice_result')


]
