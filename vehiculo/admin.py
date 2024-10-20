from django.contrib import admin
from .models import Vehiculo

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'categoria', 'precio', 'fecha_creacion', 'fecha_modificacion')
    list_filter = ('marca', 'categoria')
    search_fields = ('modelo', 'serial_carroceria', 'serial_motor')
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    fieldsets = (
        ('Información básica', {
            'fields': ('marca', 'modelo', 'categoria')
        }),
        ('Detalles técnicos', {
            'fields': ('serial_carroceria', 'serial_motor')
        }),
        ('Información de venta', {
            'fields': ('precio',)
        }),
        ('Fechas', {
            'fields': ('fecha_creacion', 'fecha_modificacion'),
            'classes': ('collapse',)
        }),
    )

admin.site.register(Vehiculo, VehiculoAdmin)