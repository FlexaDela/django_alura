from django.db import models

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
    foto = models.CharField(max_length=100, null = False, blank=False)

    def __str__(self):
        return f'Fotografia: [{self.name}]'
    
    

