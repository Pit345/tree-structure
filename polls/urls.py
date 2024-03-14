from django.urls import path, include
from polls import views

urlpatterns = [
    path('polls/', views.index, name='index'),
    path('polls/<int:id>/', views.detail, name='detail')
]