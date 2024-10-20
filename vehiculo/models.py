from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

class Vehiculo(models.Model):
    MARCA_CHOICES = [
        ('FIAT', 'Fiat'),
        ('CHEVROLET', 'Chevrolet'),
        ('FORD', 'Ford'),
        ('TOYOTA', 'Toyota'),
    ]
    
    CATEGORIA_CHOICES = [
        ('PARTICULAR', 'Particular'),
        ('TRANSPORTE', 'Transporte'),
        ('CARGA', 'Carga'),
    ]
    
    marca = models.CharField(max_length=20, choices=MARCA_CHOICES, default='FORD')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='PARTICULAR')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [
            ("visualizar_catalogo", "Puede visualizar Catálogo de Vehículos"),
        ]

    def __str__(self):
        return f"{self.marca} {self.modelo}"

# Asegúrate de que el permiso se cree
def create_permissions(sender, **kwargs):
    from django.apps import apps
    if apps.is_installed('vehiculo'):
        from django.contrib.auth.models import Permission
        from django.contrib.contenttypes.models import ContentType

        content_type = ContentType.objects.get_for_model(Vehiculo)
        Permission.objects.get_or_create(
            codename='visualizar_catalogo',
            name='Puede visualizar Catálogo de Vehículos',
            content_type=content_type,
        )

models.signals.post_migrate.connect(create_permissions)
