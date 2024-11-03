from django.contrib import admin
from inicio.models import Libros, Usuarios

class AdministrarLibros(admin.ModelAdmin):
    list_display = ('id_libro', 'nombre')
    search_fields = ('id_libro', 'nombre')  
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id_libro')
    list_per_page=5
    list_display_links=('id_libro','nombre')


admin.site.register(Libros, AdministrarLibros)

class AdministrarUsuarios(admin.ModelAdmin):
    list_display = ('id_usuario', 'nombre')  
    search_fields = ('id_usuario', 'nombre') 
    date_hierarchy = 'created'  
    readonly_fields = ('created', 'id_usuario')
    list_display_links=('id_usuario','nombre')

admin.site.register(Usuarios, AdministrarUsuarios)

