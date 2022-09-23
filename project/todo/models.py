from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titel = models.CharField(max_length=50)
    discription = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titel

    class Meta:
        ordering = ['complete']