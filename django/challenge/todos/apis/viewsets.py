from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet

from todos.apis.serializers import TodoSerializer
from todos.models import Todo

from rest_framework import generics
from .serializers import UserSerializer
from ..models import CustomUser  # Adjust the import according to your structure

class UserUpdateAPI(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserDeleteAPI(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class TodoViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['effort', 'date']
    search_fields = ['description', ]
