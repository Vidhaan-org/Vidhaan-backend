# Generated by Django 4.1 on 2022-08-25 12:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('case', '0001_initial'),
        ('permuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackcases',
            name='action_taken_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='action_taken_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trackcases',
            name='case',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='case_track', to='case.case'),
        ),
        migrations.AddField(
            model_name='order',
            name='judge',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='permuser.judge'),
        ),
        migrations.AddField(
            model_name='notification',
            name='case',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='case_notifications', to='case.case'),
        ),
        migrations.AddField(
            model_name='notification',
            name='notify_to',
            field=models.ManyToManyField(blank=True, default='', null=True, related_name='action_notify_to', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='iadetails',
            name='party',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='history',
            name='judge',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='permuser.judge'),
        ),
        migrations.AddField(
            model_name='documentdetails',
            name='advocate',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='permuser.advocate'),
        ),
        migrations.AddField(
            model_name='documentdetails',
            name='filed_by',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='case',
            name='act',
            field=models.ManyToManyField(blank=True, null=True, related_name='case_act', to='permuser.act'),
        ),
        migrations.AddField(
            model_name='case',
            name='advocate',
            field=models.ManyToManyField(blank=True, null=True, related_name='case_advocate', to='permuser.advocate'),
        ),
        migrations.AddField(
            model_name='case',
            name='document',
            field=models.ManyToManyField(blank=True, default='', null=True, related_name='case_document', to='case.documentdetails'),
        ),
        migrations.AddField(
            model_name='case',
            name='history',
            field=models.ManyToManyField(blank=True, default='', null=True, related_name='case_history', to='case.history'),
        ),
        migrations.AddField(
            model_name='case',
            name='ia',
            field=models.ManyToManyField(blank=True, default='', null=True, related_name='ia_details', to='case.iadetails'),
        ),
        migrations.AddField(
            model_name='case',
            name='objection',
            field=models.ManyToManyField(blank=True, default='', null=True, related_name='case_objection', to='case.objection'),
        ),
        migrations.AddField(
            model_name='case',
            name='order',
            field=models.ManyToManyField(blank=True, default='', null=True, related_name='case_order', to='case.order'),
        ),
        migrations.AddField(
            model_name='case',
            name='person_involved',
            field=models.ManyToManyField(blank=True, default='', null=True, related_name='person_involved', to='permuser.personinvolved'),
        ),
        migrations.AddField(
            model_name='case',
            name='petitioner',
            field=models.ManyToManyField(blank=True, null=True, related_name='case_petitioner', to='permuser.petitioner'),
        ),
        migrations.AddField(
            model_name='case',
            name='respondent',
            field=models.ManyToManyField(blank=True, null=True, related_name='case_respondent', to='permuser.respondent'),
        ),
    ]
