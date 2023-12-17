from rest_framework import serializers
from todos.models import Todo

from ..models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['date', 'description', 'is_completed', 'effort']
