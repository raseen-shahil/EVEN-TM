from django.urls import path
from.import views
urlpatterns=[
    path('register/',views.user,name='register'),
     path('login/',views.login,name='login'),
     path ('logout',views.logout,name='logout'),
]