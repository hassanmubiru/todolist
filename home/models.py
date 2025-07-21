from django.db import models

# Create your models here.
class Home(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title