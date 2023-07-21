from rest_framework import serializers
from django.contrib.auth import get_user_model,authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=('email','name','password')
        extra_kwargs={
            'password':{
                'write_only':True,
                'min_length':8
            }
        }

    def create(self,validated_data):
        email=validated_data['email']
        password=validated_data['password']
        user=authenticate(request=self.context.get('request'),email=email,password=password)
        if not user:
            return get_user_model().objects.create_user(**validated_data)
        else:
            raise serializers.ValidationError("Email already exists")
        
    def update(self,instance,validated_data):
        password=self.validated_data.pop('password',None)
        user=super().update(instance,validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user
    

class UserTokenSerializer(serializers.Serializer):
    email=serializers.EmailField(max_length=255)
    password=serializers.CharField(max_length=255,style={
        'input_type':'password'
    },
    trim_whitespace=False
    )
    def validate(self,attrs):
        email=attrs.get('email')
        password=attrs.get('password')
        user=authenticate(request=self.context.get('request'),email=email,password=password)
        if not user:
            raise serializers.ValidationError("Invalid username or password")
        attrs['user']=user
        return attrs
        