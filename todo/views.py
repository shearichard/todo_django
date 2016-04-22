from django.shortcuts import render

from rest_framework import viewsets
from .models import TodoItem
from .serializers import TodoItemSerializer


class TodoItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows TodoItems to be CRUDed.
    """
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
