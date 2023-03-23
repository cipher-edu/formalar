from django.db import models
from django.urls import reverse
import uuid
# Create your models here.
class Register(models.Model):

    user_name = models.CharField(max_length=30, verbose_name="Foydalanuvchining ismi")
    user_lastname = models.CharField(max_length=30, verbose_name="Foydalanuvchining familiyasi")
    user_age = models.IntegerField(verbose_name="Foydalanuvchining yoshi")
    user_workplace = models.CharField(max_length=30, verbose_name="Foydalanuvchining ishjoyi")
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)


    def __str__(self):
        return self.user_name