from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from app.models import UserProfile

User = get_user_model()


@receiver(post_save, sender=User)
def user_profile(sender, instance, **kwargs):
    UserProfile.objects.create(user=instance)
