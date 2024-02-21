from django.urls import path
from .views import home_page, Register_user, Login

urlpatterns = [
    path('', home_page, name='home'),
    path('register', Register_user.as_view(), name='Register'),
    path('login', Login.as_view(), name='login')

]

#
#
