from django.urls import path
from . import views

app_name = 'fit'
urlpatterns = [
    path('', views.index, name='index'),
    path('stepsAdded', views.stepsAdded, name='stepsAdded'),
    path('results', views.results, name='results'),
]
