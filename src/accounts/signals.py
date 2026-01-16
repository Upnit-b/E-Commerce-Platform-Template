from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Account, UserProfile

# auto creating user profile when account is created
@receiver(post_save, sender=Account)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
