# Generated by Django 4.1 on 2022-08-26 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0006_alter_case_case_type_alter_history_judge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='case',
        ),
        migrations.AddField(
            model_name='notification',
            name='case',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='case_notifications', to='case.case'),
        ),
    ]
