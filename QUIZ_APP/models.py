from django.db import models

# Create your models here.
# class QuesModel(models.Model):
#     question = models.CharField(max_length=200,null=True)
#     op1 = models.CharField(max_length=200,null=True)
#     op2 = models.CharField(max_length=200,null=True)
#     op3 = models.CharField(max_length=200,null=True)
#     op4 = models.CharField(max_length=200,null=True)
#     ans = models.CharField(max_length=200,null=True)
    
#     def __str__(self):
#         return self.question

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category
    

class Question(models.Model):
    choice = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=100)
    option_one = models.CharField(max_length=100)
    option_two = models.CharField(max_length=100)
    option_three = models.CharField(max_length=100, blank=True)
    option_four = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question