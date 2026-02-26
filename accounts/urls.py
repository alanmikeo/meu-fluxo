from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from .views import home_view

urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='accounts/login.html',
        redirect_authenticated_user=True,
    ), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', home_view, name='home'),
]
