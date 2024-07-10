from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass

class Question(models.Model):
    QUESTION_TYPES = [
        ('simple', 'Simple Answer'),
        ('mcq', 'Multiple Choice'),
    ]
    text_content = models.TextField()
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.text_content
