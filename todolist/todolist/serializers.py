from rest_framework import serializers
from .models import Task, UrgencyLevel, PriorityLevel, AvoidanceLevel, Status

class UrgencyLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UrgencyLevel
        fields = '__all__'

class PriorityLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriorityLevel
        fields = '__all__'

class AvoidanceLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvoidanceLevel
        fields = '__all__'

class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    urgency_level = UrgencyLevelSerializer(read_only=True)
    priority_level = PriorityLevelSerializer(read_only=True)
    avoidance_level = AvoidanceLevelSerializer(read_only=True)
    status = StatusSerializer(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'


