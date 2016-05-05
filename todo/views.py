from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import TodoItem
from .serializers import TodoItemSerializer


class TodoItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows TodoItems to be CRUDed.
    """
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
