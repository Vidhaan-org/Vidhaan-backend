from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *

from email import message
from typing import List
from .serializers import *
from .models import *
from django_filters.rest_framework import *
from django.core.mail import send_mail
import os
from twilio.rest import Client

auth_token="b7c11faeae60069df62e956c034e1713"
account_sid="ACe3d5aa8ec8a8386da8303aa756091dcc"

# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)


    # case.Case.None
@receiver(post_save, sender=Notification)
def notify_case_updates(sender, instance, created,**kwargs):
    if instance.notify_type=='New Case Update':
        # sending mail
        send_mail(
            'Case Update',
            f'There is new update on the {instance.case}. Visit the website to get more info about it!',
            'vidhaan.inbox@gmail.com',
            ['suryansh.1191@gmail.com', 'rahulkesharwani353@gmail.com', 'sonaljain067@gmail.com', 'dewansh.dt@gmail.com', 'emailanubhavagrawal@gmail.com']
        ) 

        # sending sms
        # message = client.messages \
        # .create(
        #     body=f"There is new update on the {instance.case}. Visit the website to get more info about it!'",
        #     from_='+19786629400',
        #     to='+918962245000'
        #     )

    if instance.notify_type=='Doc Deadline': 
        # sending mail
        send_mail(
            'Case Update',
            f'It\'s Last date to submit your documents of case {instance.case}',
            'vidhaan.inbox@gmail.com',
            ['suryansh.1191@gmail.com', 'rahulkesharwani353@gmail.com', 'sonaljain067@gmail.com', 'dewansh.dt@gmail.com', 'emailanubhavagrawal@gmail.com']
        ) 

        # sending sms
        # message = client.messages \
        # .create(
            # body=f'It\'s Last date to submit your documents for your case {instance.case}',
            # from_='+19786629400',
            # to='+919179322789'
            # ) 
        print('Doc Deadline')

    if instance.notify_type=='Hearing Update': 
        # sending mail
        send_mail(
            'Case Update',
            f'There is new hearing update on the {instance.case}. Visit the website to get more info about it!',
            'vidhaan.inbox@gmail.com',
            ['suryansh.1191@gmail.com', 'rahulkesharwani353@gmail.com', 'sonaljain067@gmail.com', 'dewansh.dt@gmail.com', 'emailanubhavagrawal@gmail.com']
        ) 

        # sending sms
        # message = client.messages \
        # .create(
        #     body=f'There is new hearing update on the {instance.case}. Visit the website to get more info about it!',
        #     from_='+19786629400',
        #     to='+919179322789'
        #     )
        print('Hearing Update')

    if instance.notify_type=='Next Hearing': 
        # sending mail
        send_mail(
            'Case Update',
            f'The next hearing date for case {instance.case} is updated. Visit the website to get more info about it!',
            'vidhaan.inbox@gmail.com',
            ['suryansh.1191@gmail.com', 'rahulkesharwani353@gmail.com', 'sonaljain067@gmail.com', 'dewansh.dt@gmail.com', 'emailanubhavagrawal@gmail.com']
        ) 

        # sending sms
        # message = client.messages \
        # .create(
        #     body=f'The next hearing date for case {instance.case} is updated. Visit the website to get more info about it!',
        #     from_='+19786629400',
        #     to='+919179322789'
        #     )

        print('Next Hearing')
        
    if instance.notify_type=='Hearing in 2 days': 
        # sending mail
        send_mail(
            'Case Update',
            f'The next hearing date is on 2 days for the case {instance.case}. Visit the website to get more info about it!',
            'vidhaan.inbox@gmail.com',
            ['suryansh.1191@gmail.com', 'rahulkesharwani353@gmail.com', 'sonaljain067@gmail.com', 'dewansh.dt@gmail.com', 'emailanubhavagrawal@gmail.com']
        ) 

        # sending sms
        # message = client.messages \
        # .create(
        #     body=f'The next hearing date is on 2 days for the case {instance.case}. Visit the website to get more info about it!',
        #     from_='+19786629400',
        #     to='+919179322789'
        #     )
        print('Hearing in 2 days')


@receiver(post_save, sender=Petition)
def add_approved_case(sender, instance, created,**kwargs):
    if created: pass 

