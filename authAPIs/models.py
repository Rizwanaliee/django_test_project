from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.

class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, fullName, password, **other_fields):
        # other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        return self.create_user(email, fullName, password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
    fullName = models.CharField(max_length=255, null=True)
    mobileNo = models.CharField(max_length=255, unique=True, null=False)
    email = models.EmailField(max_length=255, unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    dateOfBirth = models.CharField(max_length=255, null=True, default=None)
    isActive = models.BooleanField(default=True)
    isDeleted = models.BooleanField(default=False)
    countryCode = models.CharField(max_length=255, null=True)
    deviceToken = models.CharField(max_length=255, null=True)
    profileImage = models.CharField(max_length=255, null=True, blank=True)
    createdAt = models.DateTimeField(default=now, editable=False)
    updatedAt = models.DateTimeField(default=now, editable=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName', 'lastName', 'mobileNo']
    objects = CustomAccountManager()

    class Meta:
        db_table = 'users'
