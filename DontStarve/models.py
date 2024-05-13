from django.db import models

class Character(models.Model):
    name = models.CharField(max_length=20) #CharField()는 max_length 필수
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True) #데이터 만들어질 때 자동으로 날짜, 시간 기록
    updated_at = models.DateTimeField(auto_now=True) #데이터 수정할 때 자동으로 날짜, 시간 기록