from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    choices = models.Choices('Food', 'Entertainment', 'Other',)

class Expense(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=10)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Budget(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    budget_amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField()

