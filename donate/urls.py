from django.urls import path
from . import views

urlpatterns = [
    path('give/', views.give, name='give'),
    path('invest/', views.invest, name='invest'),
    path('give/project-of-month/', views.giveMonth, name='givemonth'),
    path('invest/project-of-month/', views.investMonth, name='investmonth')
]