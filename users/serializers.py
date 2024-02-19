from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    def validate_email(self, value):
        """
        Check if the email is unique.

        This method will be called during validation to ensure the uniqueness of the email field.
        """
        if User.objects.filter(email=value).exists():
            raise ValidationError("Email address must be unique.")
        return value