# Generated by Django 4.1 on 2022-08-26 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('case', '0003_alter_case_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='case_user', to=settings.AUTH_USER_MODEL),
        ),
    ]