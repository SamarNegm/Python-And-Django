from rest_framework import serializers
from .models import Student, Track


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'fname', 'lname', 'age', 'std_track']


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['track_name']
