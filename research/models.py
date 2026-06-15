from django.db import models
from django.contrib.auth.models import User


class ResearchSession(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    topic = models.CharField(
        max_length=500
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    plan = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.topic