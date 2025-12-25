from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.

class Fotografia(models.Model):

    CATEGORY_CHOICES = (
        ("NEBULOSA", "nebulosa"),
        ("ESTRELA","estrela"),
        ("GALAXIA","galaxia"),
        ("PLANETA","planeta")
    )


    name = models.CharField(max_length=100, null = False, blank=False)
    legenda = models.CharField(max_length=100, null = False, blank=False)
    categoria = models.CharField(max_length=100, default='', choices=CATEGORY_CHOICES)
    descricao = models.TextField(null = False, blank=False)
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicado = models.BooleanField(default=True)
    data_fotografia = models.DateField(default=datetime.now, blank=False)
    usuario = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=False, related_name="user")

    def __str__(self):
        return f'{self.name}'
    
    

