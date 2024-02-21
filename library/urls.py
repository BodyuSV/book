from django.urls import path
from .views import home_page, Register_user

urlpatterns = [
    path('', home_page, name='home'),
    path('register', Register_user.as_view(), name='Register'),
]

#
#
