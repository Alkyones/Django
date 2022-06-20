from rest_framework import serializers
from .models import registeredUserModel

class registeredUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = registeredUserModel
        fields = '__all__'

