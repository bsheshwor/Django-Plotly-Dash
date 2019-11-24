from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import (
    AbstractBaseUser
)

class CustomUser(AbstractBaseUser):
    pass

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_balance = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    account_date =  models.DateField(null=True, blank=True)
    cash_balance = models.DecimalField(max_digits=12, decimal_places=2, null=True)
    transaction_date = models.DateField(null=True, blank=True)
    transaction_type = models.CharField(max_length=30)
    transaction_amount = models.DecimalField(max_digits=12, decimal_places=2, null=True)


