from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserProfileManager(BaseUserManager):
    '''Manager for user profile'''

    def create_user(self, email, name, password=None):
        '''Create a new user profile'''
        if not email:
            raise ValueError('Please provide email address')
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        '''Create and save a new superuser'''
        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self.__db)
        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    ''' Customized User Model for Django'''
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    # error if not provided
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_short_name(self):
        '''Returns the short name of the user'''
        return self.name

    def __str__(self):
        '''Returns a string representation of the user'''
        return self.email
