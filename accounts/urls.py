
from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_User,name='login'),
    path('register/',views.register,name='register'),
    # path('')
    # path('register',views.register,name='register')
    
]
