from django.contrib import admin
from inicio.models import Libros, Usuarios, Reseñas, Grupos, Categorias, Libros_Categorias, Descargas,Ver_Libros,ComentarioContacto

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

class AdministrarLibrosCategoria(admin.ModelAdmin):
    from django.contrib import admin
from .models import Libros_Categorias

class AdministrarLibros_Categorias(admin.ModelAdmin):
    list_display = ('libro', 'categoria')
    search_fields = ('libro', 'categoria')
    date_hierarchy = 'created'
    list_per_page = 5
    list_display_links = ('libro', 'categoria')

admin.site.register(Libros_Categorias, AdministrarLibros_Categorias)



class AdministrarDescargas(admin.ModelAdmin):
    list_display = ('id_descarga','libro')
    search_fields = ('id_descarga','libro')
    date_hierarchy = 'created'
    readonly_fields = ('created','id_descarga')
    list_per_page=5
    list_display_links=('id_descarga','libro')


admin.site.register(Descargas, AdministrarDescargas)

class AdministrarVer_Libros(admin.ModelAdmin):
    list_display = ('id_ver_libro', 'usuario')
    search_fields = ('id_ver_libro', 'usuario')
    date_hierarchy = 'created'
    readonly_fields = ('id_ver_libro', 'usuario')  # Asegúrate de que readonly_fields sea una lista o tupla
    list_per_page = 5


admin.site.register(Ver_Libros, AdministrarVer_Libros)

class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'mensaje')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
   
admin.site.register(ComentarioContacto, AdministrarComentariosContacto)