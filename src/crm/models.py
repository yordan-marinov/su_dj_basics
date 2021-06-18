from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Lead(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    age = models.PositiveIntegerField(default=1)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.user.usernamel
