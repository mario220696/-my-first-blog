from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:pk>', views.post_detail, name='post_detail'),
	path(r'^post/new/', views.post_new, name='post_new'),
]