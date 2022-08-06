# Generated by Django 4.0.6 on 2022-08-06 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permuser', '0006_act_personinvolved_petitioner_respondent_and_more'),
        ('petitionFiling', '0009_remove_petition_act_remove_petition_petitioner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petitioner',
            name='petition',
        ),
        migrations.RemoveField(
            model_name='respondent',
            name='petition',
        ),
        migrations.AddField(
            model_name='petition',
            name='act',
            field=models.ManyToManyField(blank=True, null=True, related_name='petition_act', to='permuser.act'),
        ),
        migrations.AddField(
            model_name='petition',
            name='petitioner',
            field=models.ManyToManyField(blank=True, null=True, related_name='petition_petitioner', to='permuser.petitioner'),
        ),
        migrations.AddField(
            model_name='petition',
            name='respondent',
            field=models.ManyToManyField(blank=True, null=True, related_name='petition_respondent', to='permuser.respondent'),
        ),
        migrations.DeleteModel(
            name='Act',
        ),
        migrations.DeleteModel(
            name='Petitioner',
        ),
        migrations.DeleteModel(
            name='Respondent',
        ),
    ]
