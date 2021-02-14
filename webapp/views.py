
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.


from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
# Create your views here.


class MemberListView(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = Memberserializer



class ActivityListView(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = Activityserializer


