from django.shortcuts import render
from rest_framework import generics
from .serializers import BucketlistSerializer
from .models import Bucketlist

# Create your views here.

class CreateView(generics.ListCreateAPIView):
    """This class defines the behavior of our rest api
    The ListCreateAPIView is a generic view which provides GET (list all) and POST method handlers
    we specifed the queryset and serializer_class attributes.
    We also declare a perform_create method that aids in saving a new bucketlist once posted."""


    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating bucketlist"""

        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):

    #This class handles the http GET, PUT and DELETE requests and only one POST

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

