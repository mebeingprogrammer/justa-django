from django.contrib import admin
from .models import productos
from .models import Usuarios
from .models import posts

# Register your models here.
class productosAdmin(admin.ModelAdmin):
    list_display= ('perro','gato','caballo',)

class usuariosAdmin(admin.ModelAdmin):
    list_display = ('Nombre','email','password',)

class postsAdmin(admin.ModelAdmin):
    list_display = ('image','caption','created_at',)

admin.site.register(productos, productosAdmin)
admin.site.register(Usuarios, usuariosAdmin)
admin.site.register(posts, postsAdmin)
