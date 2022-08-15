from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

@receiver(post_save, sender=Notification)
def create_loan_details_db(sender, instance, created,**kwargs):
    if created: 
        if instance.notify_type=='New Case Update': 
            pass 
        if instance.notify_type=='Doc Deadline': pass 
        if instance.notify_type=='Hearing Update': pass 
        if instance.notify_type=='Next Hearing': pass 
        

