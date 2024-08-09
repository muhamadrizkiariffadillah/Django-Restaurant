from django.db import models
from accounts.models import User, UserProfile
# Create your models here.


class Vendor(models.Model):
    """

    """
    user = models.OneToOneField(
        User, related_name="user", on_delete=models.CASCADE)
    user_profile = models.OneToOneField(
        UserProfile, related_name="user_profile", on_delete=models.CASCADE)
    vendor_name = models.CharField(unique=True, max_length=255)
    vendor_license = models.ImageField(upload_to='vendor/license')
    is_approved = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.vendor_name)

    