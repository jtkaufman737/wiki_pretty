from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from wiki_pretty.scraper.serializers import * 
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class WikiViewSet(viewsets.ModelViewSet):
    """
    API endpoint that displays scraped wikipedia content
    """
    queryset = Wiki.objects.all().order_by('name')
    serializer_class = WikiSerializer
