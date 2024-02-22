from django.urls import path
from .views import home_page, Register_user, Login, logout_user, List_book

urlpatterns = [
    path('', List_book.as_view(), name='home'),
    path('register', Register_user.as_view(), name='Register'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout_user, name='logout')

]

#
#
