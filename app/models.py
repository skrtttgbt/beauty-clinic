from datetime import datetime
import uuid

import os
from shutil import copyfile
from django.conf import settings
from django.db import IntegrityError, models
from django.forms import ValidationError
from django.utils import timezone
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from app.custom_fields import PhoneNumberField
from app.managers import CustomUserManager
from django.utils.http import int_to_base36
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


ID_LENGTH = 30
DEVICE_ID_LENGTH = 15


def id_gen() -> str:
    """Generates random string whose length is `ID_LENGTH`"""
    return int_to_base36(uuid.uuid4().int)[:ID_LENGTH]

mobile_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',  # You can customize this regex pattern
        message="Phone number must be entered in the format: '+639999999'. Up to 15 digits allowed.",
    )

class Customer(models.Model):
    id = models.CharField(max_length=ID_LENGTH,
                          primary_key=True, default=id_gen)
    # Field name made lowercase.
    firstname = models.CharField(max_length=50, blank=False, default='')
    # Field name made lowercase.
    middlename = models.CharField(max_length=50, blank=True, null=True)
    # Field name made lowercase.
    lastname = models.CharField(max_length=50, blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    
    mobile = models.CharField(max_length=15, blank=True, null=True, validators=[mobile_regex])
    email = models.EmailField(
        max_length=254, unique=True, blank=False, null=False)
    picture = models.ImageField(
        upload_to='images/', blank=True, null=True, default='')

    def __str__(self):
        if not self.firstname and not self.lastname:
            return self.email
        return f'{self.firstname} {self.lastname}'

    @property
    def get_photo_url(self):
        if self.picture and hasattr(self.picture, 'url'):
            return self.picture.url
        else:
            return "/static/logo/app_icon.png"

class Gender(models.IntegerChoices):
    MALE = 0, "Male"
    FEMALE = 1, "Female"
    OTHER = 2, "Other"

class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.CharField(max_length=ID_LENGTH,
                          primary_key=True, default=id_gen, editable=False)
    email = models.EmailField(_("email address"), unique=True, blank=False)    
    firstname = models.CharField(max_length=50, blank=False, default='')
    # Field name made lowercase.
    middlename = models.CharField(max_length=50, blank=True, null=True)
    # Field name made lowercase.
    lastname = models.CharField(max_length=50, blank=True, null=True)
    gender = models.PositiveSmallIntegerField(choices=Gender.choices, default=Gender.MALE)
    phone_number = models.CharField(max_length=15, blank=True, null=True, validators=[mobile_regex])
    picture = models.ImageField(
        upload_to='images/', blank=True, null=True, default='')
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "User"

    @property
    def get_photo_url(self):
        if self.picture and hasattr(self.picture, 'url'):
            return self.picture.url
        else:
            return "/static/logo/app_icon.png"

    def __str__(self):
        if self.firstname is None and self.lastname is None:
            return self.email
        return f'{self.firstname} {self.lastname}'

class Purpose(models.IntegerChoices):
    WEDDING = 1, "Wedding"
    BAPTISM = 2, "Baptism"
    FUNERAL = 3, "Funeral"


class Status(models.IntegerChoices):
    PENDING = 1, "Pending"
    CONFIRMED = 2, "Confirmed"
    DONE = 3, "Done"
    REJECTED = 4, "Rejected"

def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

class Product(models.Model):
    name = models.CharField(unique=True, max_length=75, blank=False)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=75, blank=False)
    price = models.FloatField()
    stock = models.IntegerField(default=0)
    discount = models.FloatField(default=0)
    thumbnail = models.ImageField(
        upload_to='services/', blank=True, null=True, default='')

    def __str__(self):
        return self.name

class Payment(models.IntegerChoices):
    CASH = 1, "Cash"
    GCASH = 2, "Gcash"
    CARD = 3, "Card"


class Order(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, default=None)
    price = models.FloatField()
    discount = models.FloatField()
    quantity = models.SmallIntegerField()
    payment_method = models.PositiveSmallIntegerField(choices=Payment.choices, default=Payment.CASH)
    date = models.DateTimeField(auto_now_add=True, null=True)

class CheckoutHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_of_checkout = models.DateTimeField(default=timezone.now)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    total_quantity = models.PositiveIntegerField(default=0)

 

class AppointmentActions(models.IntegerChoices):
    PENDING = 0, "Pending"
    ACCEPT = 1, "Accept"
    DELETE = 2, "Delete"
    DECLINE = 3, "Decline"

class Service(models.Model):
    name = models.CharField(unique=True, max_length=64, blank=True, default='')
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(default=0)
    thumbnail = models.ImageField(
        upload_to='services/', blank=True, null=True, default='')
    
    def __str__(self):
        return self.name

# Skin Peeling
# Diamond Peel
# Cauteri warts removal
# Laser hair removal

class Appointment(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, default=None)
    date = models.DateTimeField(default=timezone.now, blank=False)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, default=None)
    payment_method = models.PositiveSmallIntegerField(choices=Payment.choices, default=Payment.CASH)
    status = models.PositiveSmallIntegerField(choices=AppointmentActions.choices, default=AppointmentActions.PENDING)
    action_message = models.CharField(max_length=256, blank=True, default='')

    def __str__(self):
        return f'{self.id}-{self.customer}-{self.service}'
    

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    # Add other profile fields as needed