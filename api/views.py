from django.shortcuts import render
from rest_framework import generics
from .permissions import IsOwner
from .serializers import BucketlistSerializer
from .models import Bucketlist
from rest_framework import permissions

# Create your views here.

class CreateView(generics.ListCreateAPIView):
    """This class defines the behavior of our rest api
    The ListCreateAPIView is a generic view which provides GET (list all) and POST method handlers
    we specifed the queryset and serializer_class attributes.
    We also declare a perform_create method that aids in saving a new bucketlist once posted."""


    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        """Save the post data when creating bucketlist"""

        serializer.save(owner=self.request.user)

class DetailsView(generics.RetrieveUpdateDestroyAPIView):

    #This class handles the http GET, PUT and DELETE requests and only one POST

    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwner
    )

