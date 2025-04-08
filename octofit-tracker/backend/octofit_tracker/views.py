from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from .models import User, Team, Activity, Leaderboard, Workout

def get_serializer_class():
    from .serializers import UserSerializer
    return UserSerializer

def get_team_serializer_class():
    from .serializers import TeamSerializer
    return TeamSerializer

def get_activity_serializer_class():
    from .serializers import ActivitySerializer
    return ActivitySerializer

def get_leaderboard_serializer_class():
    from .serializers import LeaderboardSerializer
    return LeaderboardSerializer

def get_workout_serializer_class():
    from .serializers import WorkoutSerializer
    return WorkoutSerializer

@api_view(['GET'])
def api_root(request, format=None):
    base_url = request.build_absolute_uri('/')
    return Response({
        'users': base_url + 'api/users/',
        'teams': base_url + 'api/teams/',
        'activities': base_url + 'api/activities/',
        'leaderboard': base_url + 'api/leaderboard/',
        'workouts': base_url + 'api/workouts/'
    })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    
    def get_serializer_class(self):
        return get_serializer_class()

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    
    def get_serializer_class(self):
        return get_team_serializer_class()

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    
    def get_serializer_class(self):
        return get_activity_serializer_class()

class LeaderboardViewSet(viewsets.ModelViewSet):
    queryset = Leaderboard.objects.all()
    
    def get_serializer_class(self):
        return get_leaderboard_serializer_class()

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    
    def get_serializer_class(self):
        return get_workout_serializer_class()
