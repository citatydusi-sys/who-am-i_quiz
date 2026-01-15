from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('quiz/<int:level_id>/', views.quiz, name='quiz'),
]