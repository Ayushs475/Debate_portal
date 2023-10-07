from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class Debate(models.Model):
    topic = models.CharField(max_length=255)
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=[('Open', 'Open'), ('Closed', 'Closed')])

    def __str__(self):
        return self.topic


class Vote(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    debate = models.ForeignKey(Debate, on_delete=models.CASCADE)
    vote_type = models.CharField(max_length=8, choices=[('Upvote', 'Upvote'), ('Downvote', 'Downvote')])

    def __str__(self):
        return f"{self.user} - {self.debate} - {self.vote_type}"

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    role = models.CharField(max_length=20, choices=[('Moderator', 'Moderator'), ('Debater', 'Debater')])
    bio = models.TextField(blank=True)
    points = models.IntegerField(default=0)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['role']

    def __str__(self):
        return self.username


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'role', 'bio', 'points')

