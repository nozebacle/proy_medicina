import os
import random
import sys
from django.conf import settings
from django.db import models
from django.db.models import Count
from django.contrib.auth.hashers import PBKDF2PasswordHasher

class Usuario(models.Model):
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=200)
    nombre = models.CharField(max_length=120)
    
