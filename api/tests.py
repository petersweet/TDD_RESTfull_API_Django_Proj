from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Bucketlist
from django.contrib.auth.models import User

# Create your tests here.
class ModelTestCase(TestCase):

    def setUp(self):
        self.bucketlist_name = "World class code"
        user = User.objects.create(username = "nerd")
        self.bucketlist = Bucketlist(name = self.bucketlist_name, owner = user)

    def test_model_create_bucketlist(self):
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count,new_count)

class ViewTestCase(TestCase):

    def setUp(self):
        """define the test client and other test vars"""

        user = User.objects.create(username="nerd")
        self.client = APIClient()
        self.client.force_authenticate(user = user)

        self.bucketlist_data = {'name': 'Hello mzfk', 'owner': user.id}
        self.responce = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format = 'json')

    def test_api_POST_a_bucketlist(self):
        """test of creation bucketlist"""

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_authenticate(self):
        new_client = APIClient
        res = new_client.get('/bucketlist/', kwargs = {'pk':3}, format = "json")
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_api_GET_a_bucketlist(self):
        """Test the api can get a given bucketlist."""

        bucketlist = Bucketlist.objects.get(id=1)
        responce = self.client.get(
            '/bucketlist/',
             kwargs={'pk': bucketlist.id},
            format = "json"
        )

        self.assertEqual(responce.status_code, status.HTTP_200_OK)
        self.assertContains(responce, bucketlist)

    def test_api_UPDATE_a_bucketlist(self):
        """Test the api can update a given bucketlist."""

        bucketlist = Bucketlist.objects.get()
        change_bucketlist = {'name': 'Smth n'}
        res = self.client.put(
            reverse('details',
                    kwargs={'pk': bucketlist.id}),
            change_bucketlist,
            format="json"
        )

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_DELETE_a_bucketlist(self):
        """Test the api can delete a given bucketlist."""

        bucketlist = Bucketlist.objects.get()
        response = self.client.delete(
            reverse('details',
                    kwargs={'pk': bucketlist.id}),
            format="json",
            follow=True
        )

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)