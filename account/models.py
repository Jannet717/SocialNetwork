from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, username, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.create_activation_code()
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email)
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class MyUser(AbstractUser):
    username = models.CharField(max_length=155, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=250)
    avatar = models.ImageField(upload_to='users', blank=True, null=True)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=6, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyUserManager()

    def __str__(self):
        return f'{self.username} {self.email}'

    def create_activation_code(self):
        import hashlib
        string = self.email + str(self.id)
        encode_string = string.encode()
        md5_object = hashlib.md5(encode_string)
        activation_code = md5_object.hexdigest()
        self.activation_code = activation_code
