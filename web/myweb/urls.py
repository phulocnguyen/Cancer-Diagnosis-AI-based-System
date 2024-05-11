from django.urls import path

from . import views

urlpatterns = [

	path('', views.index, name="home"),
	path('abstract/', views.abstract, name="abstract"),
	path('contact/', views.contact, name="contact"),
	path('dashboard/', views.dashboard, name="dashboard"),
	path('login/', views.login_view, name="login"),
	path('preview/', views.preview, name="preview"),
	path('signup/', views.signup, name="signup"),
	path('upload/', views.upload, name="upload"),
    path('account/', views.account, name="account"),
	path('logout/', views.logout_view, name='logout'),
   	path('prediction/', views.prediction_view, name='prediction'),
]