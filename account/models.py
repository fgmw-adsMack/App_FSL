from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from localflavor.br.br_states import STATE_CHOICES


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=150)
    date_of_birth = models.DateField(null=True)
    state = models.CharField(max_length=16, choices=STATE_CHOICES)
    city = models.CharField(max_length=150)
    photo = models.ImageField(upload_to ='users/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.user.username


# Atualiza autómaticamente nosso Profile quando mudar instâncias do User
@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
