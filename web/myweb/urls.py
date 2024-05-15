from django.urls import path

from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('account/', views.account_view, name="account"),
    path('logout/', views.logout_view, name='logout'),
    path('prediction/', views.prediction_view, name='prediction_view'),
]