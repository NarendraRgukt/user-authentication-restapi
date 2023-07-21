from rest_framework.generics import RetrieveUpdateAPIView,CreateAPIView
from rest_framework import authentication,permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login,get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from google.auth.transport import requests
from google.oauth2 import id_token
from django.conf import settings
from django.urls import reverse


from account import serializers
import requests

class UserCreate(CreateAPIView):
    serializer_class=serializers.UserSerializer

class UserManage(RetrieveUpdateAPIView):
    serializer_class=serializers.UserSerializer
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    def get_object(self):
        return self.request.user

class UserToken(ObtainAuthToken):
    serializer_class=serializers.UserTokenSerializer
    renderer_classes=api_settings.DEFAULT_RENDERER_CLASSES
    



class Google(TemplateView):
    template_name="account/google.html"


class GoogleAuthView(APIView):
    def get(self, request):
        # Redirect the user to the Google login page
        redirect_uri = reverse('google-auth-callback')
        auth_url = f"https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={settings.GOOGLE_OAUTH2_CLIENT_ID}&redirect_uri={request.build_absolute_uri(redirect_uri)}&scope=openid%20email&access_type=offline"
        return redirect(auth_url)

class GoogleAuthCallbackView(APIView):
    def get(self, request):
        # Handle the callback after the user grants access to their Google account
        code = request.GET.get('code')
        redirect_uri = request.build_absolute_uri(reverse('google-auth-callback'))

        # Exchange the code for an access token
        token_url = 'https://oauth2.googleapis.com/token'
        data = {
            'code': code,
            'client_id': settings.GOOGLE_OAUTH2_CLIENT_ID,
            'client_secret': settings.GOOGLE_OAUTH2_CLIENT_SECRET,
            'redirect_uri': redirect_uri,
            'grant_type': 'authorization_code',
        }

        response = requests.post(token_url, data=data)
        access_token = response.json().get('access_token')

        # Get the user info using the access token
        userinfo_url = 'https://www.googleapis.com/oauth2/v3/userinfo'
        userinfo_response = requests.get(userinfo_url, headers={'Authorization': f'Bearer {access_token}'})
        user_info = userinfo_response.json()

        # Check if the user already exists in your system using their email
        try:
            user = get_user_model().objects.get(email=user_info['email'],name=user_info['email'])
        except get_user_model().DoesNotExist:
            # User is new, create an account for them
             
            user = get_user_model().objects.create_user(email=user_info['email'], name=user_info['email'])

        # Log in the user and generate the Django auth token
        user = get_user_model().objects.get(email=user_info['email'],name=user_info['email'])
        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key,'user':user.name}, status=HTTP_200_OK)
        else:
            return Response({'error': 'Authentication failed'}, status=HTTP_400_BAD_REQUEST)