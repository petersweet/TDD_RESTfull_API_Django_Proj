from rest_framework import serializers
from .models import Bucketlist

class BucketlistSerializer (serializers.ModelSerializer):
    """Map into JSON"""

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """Meta class to map ser fields in the model"""
        model = Bucketlist

        fields = ('id',
                  'owner',
                  'name',
                  'date_created',
                  'date_modified')

        read_only_fields = ('date_created',
                            'date_modified')