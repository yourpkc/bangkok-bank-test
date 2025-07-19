from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Booking

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'user', 'booking_datetime', 'created_at']
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = instance.user.get_full_name()
        return data
