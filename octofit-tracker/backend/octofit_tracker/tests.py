from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from datetime import date

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='Test Team')
        self.user = User.objects.create(name='Test User', email='test@example.com', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='desc', difficulty='Easy')
        self.activity = Activity.objects.create(user=self.user, type='Run', duration=30, date=date.today())
        self.leaderboard = Leaderboard.objects.create(user=self.user, score=50)

    def test_api_root(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('users', response.data)

    def test_users_endpoint(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_teams_endpoint(self):
        response = self.client.get('/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_activities_endpoint(self):
        response = self.client.get('/activities/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_workouts_endpoint(self):
        response = self.client.get('/workouts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_leaderboard_endpoint(self):
        response = self.client.get('/leaderboard/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
