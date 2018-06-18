from django.db import models
from django.contrib.auth.models import (
    PermissionsMixin, AbstractBaseUser, UserManager)
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail

from rest_framework.authtoken.models import Token

# Create your models here.


class NewManager(UserManager):

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError("The email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        Token.objects.get_or_create(user=user)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_super set to True')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(
        _('email address'),
        unique=True,
        max_length=255)
    first_name = models.CharField(
        _('first name'),
        max_length=70)
    last_name = models.CharField(
        _('last name'),
        max_length=70)
    avatar = models.ImageField(
        upload_to='users/avatars/',
        null=True,
        blank=True)
    date_joined = models.DateTimeField(
        _('date joined'),
        auto_now_add=True)
    is_active = models.BooleanField(
        _('active'),
        default=True)
    is_staff = models.BooleanField(
        _('staff'),
        default=False)

    objects = NewManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = "{0} {1}".format(self.first_name, self.last_name)
        return full_name

    def get_short_name(self):
        short_name = "{0}".format(self.first_name)
        return short_name

    def __str__(self):

        return self.email
