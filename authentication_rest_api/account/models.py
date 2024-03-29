
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self,email,name=None,password=None):
        if not email:
            raise ValueError("please provide the email")
        email=self.normalize_email(email)
        user=self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)
        user.is_active=True
        return user
    def create_superuser(self,email,name,password=None):
        user=self.create_user(email,name,password)
        user.is_active=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=['name']
    objects=UserManager()
    
    def get_fullname(self):
        return self.name
    
    def __str__(self):
        return self.email
    