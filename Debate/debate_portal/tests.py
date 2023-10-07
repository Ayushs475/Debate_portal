from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User  # Use your custom user model if applicable
from .models import CustomUser, Debate, Vote  # Import your models
from .serializers import CustomUserSerializer, DebateSerializer, VoteSerializer

class YourTestCase(APITestCase):
    def setUp(self):
        # Create a test user with a token
        self.user = CustomUser.objects.create(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Create sample data for testing
        self.debate_data = {'topic': 'Sample Debate Topic'}
        self.vote_data = {'user': self.user.id, 'debate': 1, 'vote_type': 'Upvote'}

    def test_user_registration(self):
        url = reverse('user-registration')  # Replace 'user-registration' with your actual URL name
        response = self.client.post(url, {'username': 'newuser', 'password': 'newpassword'})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'User registered successfully')

    def test_debate_creation(self):
        url = reverse('debate-management')  # Replace 'debate-management' with your actual URL name
        response = self.client.post(url, self.debate_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Debate.objects.count(), 1)
        self.assertEqual(Debate.objects.get().topic, 'Sample Debate Topic')

    def test_vote_submission(self):
        url = reverse('vote')  # Replace 'vote' with your actual URL name
        response = self.client.post(url, self.vote_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vote.objects.count(), 1)
        self.assertEqual(Vote.objects.get().vote_type, 'Upvote')

    # Add more test cases for other views as needed
