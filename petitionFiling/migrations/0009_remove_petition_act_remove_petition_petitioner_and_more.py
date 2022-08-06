# Generated by Django 4.0.6 on 2022-08-04 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petitionFiling', '0008_alter_petition_case_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petition',
            name='act',
        ),
        migrations.RemoveField(
            model_name='petition',
            name='petitioner',
        ),
        migrations.RemoveField(
            model_name='petition',
            name='respondent',
        ),
        migrations.AddField(
            model_name='act',
            name='petition',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='petition_act', to='petitionFiling.petition'),
        ),
        migrations.AddField(
            model_name='petitioner',
            name='petition',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='petition_petitioner', to='petitionFiling.petition'),
        ),
        migrations.AddField(
            model_name='respondent',
            name='petition',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='petition_respondent', to='petitionFiling.petition'),
        ),
    ]