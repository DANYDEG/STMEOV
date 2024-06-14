from django.urls import path
from . import views

app_name = 'exam'
urlpatterns = [
    path('', views.home, name='home'),
    path('test/<int:q_id>/', views.test, name='test'),
    path('create/', views.add_candidate, name='add_candidate'),
]
