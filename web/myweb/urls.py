from django.urls import path

from . import views

urlpatterns = [

	path('', views.index, name="home"),
	path('abstract/', views.abstract, name="abstract"),
	path('contact/', views.contact, name="contact"),
	path('dashboard/', views.dashboard, name="dashboard"),
	path('login/', views.login, name="login"),
	path('preview/', views.preview, name="preview"),
	path('signup/', views.signup, name="signup"),
	path('upload/', views.upload, name="upload"),

]