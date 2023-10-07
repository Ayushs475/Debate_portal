from rest_framework import serializers
from .models import CustomUser,debate,vote

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'role', 'bio', 'points')


class DebateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debate
        fields = '__all__'  # Serialize all fields in the Debate model

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'  # Serialize all fields in the Vote model

