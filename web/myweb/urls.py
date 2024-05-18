from django.urls import path

from . import views

urlpatterns = [
	path('', views.home, name="home"),
	path('account/', views.account_view, name="account_view"),
    path('logout/', views.logout_view, name='logout'),
    path('detection/', views.prediction_view, name='prediction_view'),
    path("verify-email/<slug:username>", views.verify_email, name="verify-email"),
    path("resend-otp/", views.resend_otp, name="resend-otp"),
    path('prediction_history/', views.prediction_history_view, name='prediction_history'),
]