from django.contrib import admin
from .models import Fotografia


@admin.register(Fotografia)
class FotografiaAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "legenda", "publicado") # vai mostrar estes campos
    list_display_links = ("id", "name") # vai adicionar um link nestes campos
    search_fields = ("name",) #ele precisa ser uma tupla e adiciona a aba de buscar pelo nome
    list_filter = ("categoria",) #adiciona filtro por categora
    list_editable = ("publicado",) #permite editar diretamente no admin
    list_per_page = 10 #lista apenas 10 items por pagina

