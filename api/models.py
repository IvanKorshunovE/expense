from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator, MinLengthValidator
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)


class User(models.Model):
    # If there is a need for authentication and authorization, I'd inherit from AbstractUser or AbstractBaseUser
    username = models.CharField(
        max_length=255,
        validators=[EmailValidator(message="Enter a valid email address.")],
        unique=True,  # Ensures no duplicate emails
    )
    email = models.CharField(
        max_length=255,
        validators=[MinLengthValidator(3, message="Username should have at least 3 characters")]
    )


class Expense(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField(
        # validators=[MinValueValidator(0)]
    )  # - Be sure expense is positive
    date = models.DateTimeField(auto_now_add=True)  # I would consider adding created, updated fields instead of this
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
