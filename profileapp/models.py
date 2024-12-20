from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') #user 탈퇴 후 계정 사라짐

    image = models.ImageField(upload_to='profile/', null = True) # 프로필 사진 없어도 괜춘
    nickname = models.CharField(max_length =20, unique=True, null = True)
    message = models.CharField(max_length=100, null = True)