from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)

        # Create Workouts
        w1 = Workout.objects.create(name='Super Strength', description='Strength training for heroes', difficulty='Hard')
        w2 = Workout.objects.create(name='Flight Training', description='Aerial maneuvers and endurance', difficulty='Medium')

        # Create Activities
        Activity.objects.create(user=tony, type='Running', duration=30, date=date.today())
        Activity.objects.create(user=steve, type='Cycling', duration=45, date=date.today())
        Activity.objects.create(user=bruce, type='Martial Arts', duration=60, date=date.today())
        Activity.objects.create(user=clark, type='Flying', duration=120, date=date.today())

        # Create Leaderboard
        Leaderboard.objects.create(user=tony, score=100)
        Leaderboard.objects.create(user=steve, score=90)
        Leaderboard.objects.create(user=bruce, score=95)
        Leaderboard.objects.create(user=clark, score=110)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data!'))
