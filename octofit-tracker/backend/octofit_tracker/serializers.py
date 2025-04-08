from rest_framework import serializers
from bson import ObjectId
from django.apps import apps

def get_model(model_name):
    return apps.get_model('octofit_tracker', model_name)

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return ObjectId(data)

class UserSerializer(serializers.ModelSerializer):
    _id = ObjectIdField()

    class Meta:
        model = get_model('User')
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    _id = ObjectIdField()
    members = UserSerializer(many=True)

    class Meta:
        model = get_model('Team')
        fields = '__all__'

class ActivitySerializer(serializers.ModelSerializer):
    _id = ObjectIdField()
    user = UserSerializer()

    class Meta:
        model = get_model('Activity')
        fields = '__all__'

class LeaderboardSerializer(serializers.ModelSerializer):
    _id = ObjectIdField()
    user = UserSerializer()

    class Meta:
        model = get_model('Leaderboard')
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    _id = ObjectIdField()

    class Meta:
        model = get_model('Workout')
        fields = '__all__'
