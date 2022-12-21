from django.db import models

STATUS_CHOICES = (
    ('OPEN', 'OPEN'),
    ('NOTOPEN', 'CLOSE'),
)

class AddRoom(models.Model):
    room_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='OPEN')

    def __str__(self):
        return self.room_name       
    