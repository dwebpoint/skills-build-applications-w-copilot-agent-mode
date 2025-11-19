from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_team_creation(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_activity_creation(self):
        activity = Activity.objects.create(user='testuser', activity_type='Running', duration=30)
        self.assertEqual(str(activity), 'testuser - Running')

    def test_leaderboard_creation(self):
        leaderboard = Leaderboard.objects.create(user='testuser', points=100)
        self.assertEqual(str(leaderboard), 'testuser - 100')

    def test_workout_creation(self):
        workout = Workout.objects.create(name='Test Workout', description='Test Desc')
        self.assertEqual(str(workout), 'Test Workout')
