from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import timedelta
from bson import ObjectId

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        try:
            # Create users
            users = [
                User.objects.create(_id=ObjectId(), username='paul_octo', email='paul.octo@mergington.edu', password='pauloctopass'),
                User.objects.create(_id=ObjectId(), username='jessica_cat', email='jessica.cat@mergington.edu', password='jessicacatpass'),
                User.objects.create(_id=ObjectId(), username='student_athlete1', email='athlete1@mergington.edu', password='athlete1pass'),
                User.objects.create(_id=ObjectId(), username='student_athlete2', email='athlete2@mergington.edu', password='athlete2pass'),
                User.objects.create(_id=ObjectId(), username='student_athlete3', email='athlete3@mergington.edu', password='athlete3pass'),
            ]

            # Create teams
            team1 = Team.objects.create(_id=ObjectId(), name='Mergington Tigers')
            team2 = Team.objects.create(_id=ObjectId(), name='Mergington Lions')
            
            # Add members to teams
            team1.members.add(users[0], users[2], users[4])
            team2.members.add(users[1], users[3])

            # Create activities
            activities = [
                Activity.objects.create(_id=ObjectId(), user=users[0], activity_type='Running', duration=timedelta(minutes=45)),
                Activity.objects.create(_id=ObjectId(), user=users[1], activity_type='Swimming', duration=timedelta(hours=1)),
                Activity.objects.create(_id=ObjectId(), user=users[2], activity_type='Basketball', duration=timedelta(hours=2)),
                Activity.objects.create(_id=ObjectId(), user=users[3], activity_type='Weight Training', duration=timedelta(minutes=60)),
                Activity.objects.create(_id=ObjectId(), user=users[4], activity_type='Yoga', duration=timedelta(minutes=90)),
            ]

            # Create leaderboard entries
            leaderboard_entries = [
                Leaderboard.objects.create(_id=ObjectId(), user=users[0], score=95),
                Leaderboard.objects.create(_id=ObjectId(), user=users[1], score=88),
                Leaderboard.objects.create(_id=ObjectId(), user=users[2], score=92),
                Leaderboard.objects.create(_id=ObjectId(), user=users[3], score=85),
                Leaderboard.objects.create(_id=ObjectId(), user=users[4], score=90),
            ]

            # Create workouts
            workouts = [
                Workout.objects.create(_id=ObjectId(), name='Morning Cardio', description='Start your day with a refreshing cardio workout', difficulty='beginner', duration=timedelta(minutes=30)),
                Workout.objects.create(_id=ObjectId(), name='Strength Training 101', description='Basic strength training for beginners', difficulty='beginner', duration=timedelta(minutes=45)),
                Workout.objects.create(_id=ObjectId(), name='Team Sports', description='Group activities for team building', difficulty='intermediate', duration=timedelta(minutes=60)),
                Workout.objects.create(_id=ObjectId(), name='Flexibility Focus', description='Improve your flexibility and balance', difficulty='intermediate', duration=timedelta(minutes=45)),
                Workout.objects.create(_id=ObjectId(), name='High Intensity Circuit', description='Advanced circuit training workout', difficulty='advanced', duration=timedelta(minutes=40)),
            ]

            self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error populating database: {str(e)}'))
