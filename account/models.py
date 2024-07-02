from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from .managers import CustomUserManager
from ckeditor_uploader.fields import RichTextUploadingField

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(_("first_name"),max_length=50)
    last_name = models.CharField(_("last_name"),max_length=50)
    about = RichTextUploadingField()
    profile_photo= models.ImageField(_("photo"),upload_to="user_images", null=True,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    

    def get_absolute_url(self):
        return reverse("login")