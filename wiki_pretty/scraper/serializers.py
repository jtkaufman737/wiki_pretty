from django.contrib.auth.models import User
from rest_framework import serializers
from wiki_pretty.scraper.models import Wiki

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email','groups')

class WikiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wiki
        fields = ('name','id','content')
