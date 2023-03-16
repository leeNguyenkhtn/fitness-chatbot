from django.db import models
from django.utils import timezone
# Create your models here.

class Question (models.Model):
    question_text = models.TextField(max_length=100000, blank=False, null=False)
    time_public = models.DateTimeField(default=timezone.datetime.now())

class Answer (models.Model):
    answer_text = models.TextField(max_length=10000000)
    time_public = models.DateTimeField(default=timezone.datetime.now())
