from django.db import models

# Create your models here.

# 레시피
class Recipe(models.Model):
    # 제목 (30자로 최대 길이 제한)
    title = models.CharField(max_length=30)
    # 생성 날짜, 시간 (지동 생성)
    created_at = models.DateTimeField(auto_now_add=True)
    # 내용 (무한대. 길이제한 없음)
    content = models.TextField()

