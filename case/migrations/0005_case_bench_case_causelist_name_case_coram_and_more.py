# Generated by Django 4.1 on 2022-08-15 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('case', '0004_documentdetails_document_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='bench',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='causelist_name',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='coram',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='decision_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='district',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='judicial',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='latest_hearing',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='next_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='stage_of_case',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='case',
            name='state',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='case',
            name='case_status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('DISPOSED', 'Disposed')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='trackcases',
            name='action_taken_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='action_taken_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='CaseStatus',
        ),
    ]
