from django.contrib import admin
from inicio.models import Libros, Usuarios, Reseñas, Grupos, Categorias, Libros_Categorias

class AdministrarLibros(admin.ModelAdmin):
    list_display = ('id_libro', 'nombre')
    search_fields = ('id_libro', 'nombre')  
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id_libro')
    list_per_page=5
    list_display_links=('id_libro','nombre')


admin.site.register(Libros, AdministrarLibros)

class AdministrarGrupos(admin.ModelAdmin):
    list_display= ('id_grupo', 'nombre')
    search_fields = ('id_grupo', 'nombre')
    date_hierarchy='created'
    readonly_fields=('created', 'id_grupo')
    list_display_links=('id_grupo','nombre')

admin.site.register(Grupos, AdministrarGrupos)

class AdministrarReseñas(admin.ModelAdmin):
    list_display = ('id_reseña', 'calificacion')
    search_fields = ('id_reseña', 'calificacion')
    date_hierarchy='created'
    readonly_fields=('created', 'id_reseña')
    list_display_links=('id_reseña','calificacion')

admin.site.register(Reseñas, AdministrarReseñas)

class AdministrarUsuarios(admin.ModelAdmin):
    list_display = ('id_usuario', 'nombre')  
    search_fields = ('id_usuario', 'nombre') 
    date_hierarchy = 'created'  
    readonly_fields = ('created', 'id_usuario')
    list_display_links=('id_usuario','nombre')

admin.site.register(Usuarios, AdministrarUsuarios)

class AdministrarCategoria(admin.ModelAdmin):
    list_display = ('id_categoria', 'nombre')
    search_fields = ('id_categoria', 'nombre')  
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id_categoria')
    list_per_page=5
    list_display_links=('id_categoria','nombre')


admin.site.register(Categorias, AdministrarCategoria)

class AdministrarLibros_Categoria(admin.ModelAdmin):
    list_display = ('id_categoria', 'id_libro')
    search_fields = ('id_categoria', 'id_libro_categoria')  
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id_categoria')
    list_per_page=5
    list_display_links=('id_libro_categoria','id_libro')


admin.site.register(Libros_Categorias, AdministrarLibros_Categoria)



