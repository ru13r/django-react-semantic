from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# REST Framework
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


from .models import DRFTest
from main import serializers

# Create your views here.

class detail_view(generics.RetrieveUpdateDestroyAPIView):
    queryset = DRFTest.objects.all()
    serializer_class = serializers.DRFTestSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAdminUser,)


class list_view(generics.ListAPIView):
    queryset = DRFTest.objects.all()
    serializer_class = serializers.DRFTestSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(list_view, self).dispatch(*args, **kwargs)
    #
    # def get(self, request):
    #     content = {
    #         'user': request.user,  # `django.contrib.auth.User` instance.
    #         'auth': request.auth,  # None
    #     }
    #     return Response(content)
