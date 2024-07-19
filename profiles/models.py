from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from events.models import Event


class Profile(models.Model):
    """
    Extends default Django User model.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interested_events = models.ManyToManyField(
        Event, blank=True, related_name="interested_users")

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
