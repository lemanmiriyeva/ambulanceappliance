from django.db.models.signals import post_save, pre_delete
from django.db.models import signals
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import User
 
 

@receiver(signals.pre_save, sender=User)
def check_service(sender, instance, **kwargs):
    if instance.username=="leman":
        instance.username = 'User'
    
# post_save method
@receiver(signals.post_save, sender=User) 
def create_service(sender, instance, created, **kwargs):
    print("Save method for user is called") 