from django.db import models

# Create your models here.

# ad在登录用户中,不在这里
# 创新用户时候,群控的要新建usr验证 和 本数据库表,,,,,,单独的只在这里新建
class Auth(models.Model):
    usrName = models.CharField(max_length=200, unique=True)
    count = models.IntegerField(default=0)
    desc = models.TextField(default="Null")
    status = models.BooleanField(default=True) # True就是群控端 False就是单独的脚本控制


