# Generated by Django 4.1 on 2022-08-25 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permuser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advocate',
            name='advocate_number',
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
