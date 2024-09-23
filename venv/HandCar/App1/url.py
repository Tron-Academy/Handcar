
from django.urls import path
from . import views  # Make sure to import views from the correct app

urlpatterns = [
    # path('otp', views.generate_otp, name='generate_otp'),
    # path('sms', views.send_sms, name='send_sms'),  # Correct path definition

    path('api/login/', views.login_view, name='api-login'),
    path('api/signup/', views.signup_view, name='api-signup'),
    path('api/logout/', views.logout_view, name='api-logout'),
]
