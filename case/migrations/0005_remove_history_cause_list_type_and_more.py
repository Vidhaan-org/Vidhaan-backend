# Generated by Django 4.1 on 2022-08-26 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0004_alter_case_case_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='history',
            name='cause_list_type',
        ),
        migrations.AlterField(
            model_name='history',
            name='purpose_of_hearing',
            field=models.CharField(blank=True, choices=[('PRESENCE_WRITTEN_STATEMENT', 'Presence written statement'), ('REPLY', 'Reply'), ('ARGUMENTS', 'Arguments')], default='', max_length=50, null=True),
        ),
    ]
