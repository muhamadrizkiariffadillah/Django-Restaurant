from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models import OneToOneField


# Create your models here.


class UserManager(BaseUserManager):

    def create_user(self, first_name, last_name, username, email, password=None):
        """
        Creates and saves a new user
        :param last_name:
        :param first_name:
        :param username:
        :param email:
        :param password:
        :return:
        """
        if not first_name and last_name:
            raise ValueError('Users must have first name and last name')
        if not username:
            raise ValueError('Users must have username')
        if not email:
            raise ValueError('Users must have email')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, username, email, password=None):
        """

        :param first_name:
        :param last_name:
        :param username:
        :param email:
        :param password:
        :return:
        """
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)

        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    """

    """
    VENDOR = 1
    CUSTOMER = 2
    ROLE_CHOICE = (
        (VENDOR, 'vendor'),
        (CUSTOMER, 'customer'),
    )
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=20, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICE, blank=True, null=True)

    # required verified fields
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    # required info fields
    last_login = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name',
        'last_name',
        'username',
    ]

    objects = UserManager()

    def __str__(self):
        return str(self.username)

    def has_permissions(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class UserProfile(models.Model):
    user = OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True)
    profile_picture = models.ImageField(upload_to='users/profile_pictures', blank=True, null=True)
    cover_photo = models.ImageField(upload_to='users/cover_photo', blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    pin_code = models.CharField(max_length=6, blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.user.username


