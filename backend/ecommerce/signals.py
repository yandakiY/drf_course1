from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

@receiver(post_save , sender=User , weak=False)
def report_uploaded(instance , sender , created , **kwargs):
    if created:
        Token.objects.create(user=instance)