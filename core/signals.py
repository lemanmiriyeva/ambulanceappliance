from django.db.models import signals
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from .models import *

# pre_save method signal
@receiver(signals.pre_save, sender=Service)
def check_service(sender, instance, **kwargs):
    if not instance.title:
        instance.title = 'This is Default Title'
    
# post_save method
@receiver(signals.post_save, sender=Service) 
def create_service(sender, instance, created, **kwargs):
    print("Save method is called") 


@receiver(pre_delete, sender=Service)
def delete_related_journal(sender, instance, **kwargs):
    print("salam")





@receiver(signals.pre_save, sender=About)
def check_service(sender, instance, **kwargs):
    if not instance.title:
        instance.title = 'This is Default Title for about'
    
# post_save method
@receiver(signals.post_save, sender=About) 
def create_service(sender, instance, created, **kwargs):
    print("Save method for about is called") 