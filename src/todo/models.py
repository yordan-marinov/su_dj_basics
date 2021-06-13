from django.db import models


class Task(models.Model):
    PRIORITY_CHOICES = (
        (3, "High"),
        (2, "Medium"),
        (1, "Low"),
    )

    task = models.CharField(max_length=120)
    description = models.TextField()
    complete = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES)

    class Meta:
        ordering = ["status", 'priority']

    def __str__(self):
        return self.task
