from django.db import models
from django.contrib.auth.models import User

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_datetime = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)