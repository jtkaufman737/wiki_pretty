from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerialization(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email','groups')

class WikiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Wiki
        fields = ('name','title','id','content')
