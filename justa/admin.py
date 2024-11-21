from django.contrib import admin
from .models import productos

# Register your models here.
class productosAdmin(admin.ModelAdmin):
    list_display= ('perro','gato','caballo',)

admin.site.register(productos, productosAdmin)