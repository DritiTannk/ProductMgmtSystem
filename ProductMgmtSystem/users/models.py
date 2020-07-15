from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser, UserManager


# Create your models here.

class User(AbstractUser):
    objects = UserManager()
    first_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ['email']

    def _get_full_name_(self):
        return self.username

    def __str__(self):
        return "%s | %s " % (self.first_name, self.username)


class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
