from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserTests(APITestCase):
    def setUp(self):
        self.user_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123'
        }
        self.user = User.objects.create(**self.user_data)

    def test_create_user(self):
        url = reverse('user-list')
        response = self.client.post(url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TeamTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com')
        self.team_data = {
            'name': 'Test Team',
            'members': [self.user]
        }

    def test_create_team(self):
        url = reverse('team-list')
        response = self.client.post(url, self.team_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com')
        self.activity_data = {
            'user': self.user,
            'activity_type': 'running',
            'duration': '00:30:00'
        }

    def test_create_activity(self):
        url = reverse('activity-list')
        response = self.client.post(url, self.activity_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LeaderboardTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', email='test@example.com')
        self.leaderboard_data = {
            'user': self.user,
            'score': 100
        }

    def test_create_leaderboard_entry(self):
        url = reverse('leaderboard-list')
        response = self.client.post(url, self.leaderboard_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WorkoutTests(APITestCase):
    def setUp(self):
        self.workout_data = {
            'name': 'Test Workout',
            'description': 'Test workout description',
            'difficulty': 'medium',
            'duration': '00:45:00'
        }

    def test_create_workout(self):
        url = reverse('workout-list')
        response = self.client.post(url, self.workout_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
