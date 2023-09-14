# user_management/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from entity_manager.models import Business  # Import Business model from entity_manager

User = get_user_model()

@receiver(post_save, sender=Business)
def create_user_for_business(sender, instance, created, **kwargs):
    if created:
        # Create a user associated with the newly created business
        user = User.objects.create(
            email=f"{instance.email}",
            username=f"{instance.name.lower()}{instance.id}".replace(" ", ""),
            business=instance,
            is_active=True,
            is_staff=True,
            is_superuser=False
        )
        
        # Set the user's password using set_password to ensure it's hashed
        user.set_password("use-!@#-123")
        user.save()