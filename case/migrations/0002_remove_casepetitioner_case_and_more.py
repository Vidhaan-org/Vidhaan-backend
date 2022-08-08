# Generated by Django 4.1 on 2022-08-08 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permuser', '0006_act_personinvolved_petitioner_respondent_and_more'),
        ('case', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casepetitioner',
            name='case',
        ),
        migrations.RemoveField(
            model_name='caserespondent',
            name='case',
        ),
        migrations.RenameField(
            model_name='notification',
            old_name='web_description',
            new_name='case_description',
        ),
        migrations.RenameField(
            model_name='notification',
            old_name='title',
            new_name='case_title',
        ),
        migrations.RemoveField(
            model_name='casestatus',
            name='case',
        ),
        migrations.RemoveField(
            model_name='documentdetails',
            name='case',
        ),
        migrations.RemoveField(
            model_name='history',
            name='case',
        ),
        migrations.RemoveField(
            model_name='iadetails',
            name='case',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='is_viewed_in_mail',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='is_viewed_in_web',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='mail_description',
        ),
        migrations.RemoveField(
            model_name='objection',
            name='case',
        ),
        migrations.RemoveField(
            model_name='order',
            name='case',
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
            name='petitioner',
            field=models.ManyToManyField(blank=True, null=True, related_name='case_petitioner', to='permuser.petitioner'),
        ),
        migrations.AddField(
            model_name='case',
            name='respondent',
            field=models.ManyToManyField(blank=True, null=True, related_name='case_respondent', to='permuser.respondent'),
        ),
        migrations.AddField(
            model_name='notification',
            name='action_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='is_notification_recieved',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='notification',
            name='notification_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='casestatus',
            name='decision_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='casestatus',
            name='latest_hearing',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='casestatus',
            name='next_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.RemoveField(
            model_name='notification',
            name='case',
        ),
        migrations.DeleteModel(
            name='CaseAct',
        ),
        migrations.DeleteModel(
            name='CasePetitioner',
        ),
        migrations.DeleteModel(
            name='CaseRespondent',
        ),
        migrations.AddField(
            model_name='notification',
            name='case',
            field=models.ManyToManyField(blank=True, default='', null=True, related_name='case_notifications', to='case.case'),
        ),
    ]
