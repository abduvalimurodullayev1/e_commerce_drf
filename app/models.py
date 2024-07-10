from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("Telefon raqam bo'lishi shart!")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        user = self.create_user(phone_number, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = models.CharField(max_length=155, unique=False, null=True, blank=True)
    first_name = models.CharField(max_length=155, unique=False, null=True, blank=True)
    last_name = models.CharField(max_length=155, unique=False, null=True, blank=True)
    image = models.ImageField(upload_to='/image')
    phone_validator = RegexValidator(
        regex=r'^\+998\d{9}$',
        message="Yaroqsiz telefon raqam!"
    )
    phone_number = models.CharField(
        max_length=25,
        validators=[phone_validator],
        null=True,
        blank=True,
        unique=True
    )
    image = models.ImageField(upload_to="images", null=True, blank=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="images")
    price = models.FloatField()
    discount_price = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="orders")
    quantity = models.IntegerField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.phone_number


class MyFavourites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="favourites")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="favourites")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.phone_number

