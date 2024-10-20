from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Permission

@receiver(post_save, sender=User)
def asignar_permiso_visualizar_catalogo(sender, instance, created, **kwargs):
    if created:
        permission = Permission.objects.get(codename='visualizar_catalogo')
        instance.user_permissions.add(permission)