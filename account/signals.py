from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import user
from.models import UserProfile


def create_or_update_user_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        instance.userprofile.save()