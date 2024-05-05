from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    login_id = models.CharField(max_length=15)
    nickname = models.CharField(max_length=30)  # 닉네임 필드 추가
    is_active = models.BooleanField(default=True)  # 활성 상태 필드 추가



