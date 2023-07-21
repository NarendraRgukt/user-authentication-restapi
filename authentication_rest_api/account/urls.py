from django.urls import path
from account import views

app_name="account"

urlpatterns = [
    path('create/user/',views.UserCreate.as_view(),name="usercreate"),
    path('user/manage/',views.UserManage.as_view(),name="usermanage"),
    path('user/token/',views.UserToken.as_view(),name="usertoken"),
    path('auth/google/', views.GoogleAuthView.as_view(), name='google-auth'),
   
   
]
