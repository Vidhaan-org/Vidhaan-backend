# Generated by Django 4.0.6 on 2022-08-02 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CaseDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnr_number', models.IntegerField(unique=True)),
                ('case_type', models.CharField(max_length=50, null=True)),
                ('filling_number', models.IntegerField()),
                ('registration_number', models.IntegerField()),
                ('filling_date', models.DateField(null=True)),
                ('first_hearing_date', models.DateField(null=True)),
                ('latest_hearing', models.DateField(null=True)),
                ('decision_date', models.DateField(null=True)),
                ('case_status', models.CharField(choices=[('PENDING', 'PENDING'), ('DISPOSED', 'DISPOSED')], max_length=50)),
                ('nature_of_disposal', models.CharField(max_length=50, null=True)),
                ('coram', models.CharField(max_length=50, null=True)),
                ('bench', models.CharField(max_length=50, null=True)),
                ('judicial', models.CharField(max_length=50, null=True)),
                ('petitioner', models.CharField(max_length=50, null=True)),
                ('p_advocate', models.CharField(max_length=50, null=True)),
                ('respondent', models.CharField(max_length=50, null=True)),
                ('r_advocate', models.CharField(max_length=50, null=True)),
                ('judge', models.CharField(max_length=50, null=True)),
                ('acts', models.CharField(max_length=50, null=True)),
                ('section', models.CharField(max_length=50, null=True)),
                ('next_date', models.DateField(null=True)),
                ('history_of_case_hearing', models.TextField(null=True)),
            ],
        ),
    ]
