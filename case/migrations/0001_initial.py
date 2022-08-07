# Generated by Django 4.1 on 2022-08-07 07:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('petitionFiling', '0009_remove_petition_act_remove_petition_petitioner_and_more'),
        ('permuser', '0005_advocate_judge'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnr_number', models.IntegerField(null=True, unique=True)),
                ('case_type', models.CharField(blank=True, choices=[('ARBITRATION Original Petition', 'ARBITRATION Original Petition'), ('APPEAL SUIT', 'APPEAL SUIT'), ('ANDHRA TENANCY APPEAL', 'ANDHRA TENANCY APPEAL'), ('ANDHRA TENANCY CASE', 'ANDHRA TENANCY CASE'), ('COPY APPLICATION', 'COPY APPLICATION'), ('CALENDAR CASE-AP TRANSCO', 'CALENDAR CASE-AP TRANSCO'), ('CALENDAR CASE LAND GRABBING', 'CALENDAR CASE LAND GRABBING'), ('CIVIL MISCELLEANOUS APPEAL', 'CIVIL MISCELLEANOUS APPEAL'), ('CRIME NUMBER', 'CRIME NUMBER'), ('CRIMINAL APPEAL', 'CRIMINAL APPEAL'), ('CRIME APPEAL METROPOLITAN UNIT', 'CRIME APPEAL METROPOLITAN UNIT'), ('CRIMINAL MP', 'CRIMINAL MP'), ('CRLMP BAIL', 'CRLMP BAIL'), ('CRIMINAL REVISION PETITION', 'CRIMINAL REVISION PETITION'), ('CRML. REV PETITION METROPOLITA', 'CRML. REV PETITION METROPOLITA'), ('DOMESTIC VIOLENCE CASE', 'DOMESTIC VIOLENCE CASE'), ('Estate Abolition ACT', 'Estate Abolition ACT'), ('APPEAL UNDER EAT ACT', 'APPEAL UNDER EAT ACT'), ('EC ACT APPEALS', 'EC ACT APPEALS'), ('ECECTION OP', 'ECECTION OP'), ('ELECTRICITY MATER CASE', 'ELECTRICITY MATER CASE'), ('EXCEUTION PETITION', 'EXCEUTION PETITION'), ('ELECTRICITY SESSIONS CASE', 'ELECTRICITY SESSIONS CASE'), ('EMPLOYEES STATE INSURANCE', 'EMPLOYEES STATE INSURANCE'), ('FAMILY COURT OP', 'FAMILY COURT OP'), ('FAMILY COURT OS', 'FAMILY COURT OS'), ('GUARDIAN AND WARDS OP', 'GUARDIAN AND WARDS OP'), ('INDUSTRIAL DISPUTE', 'INDUSTRIAL DISPUTE'), ('INSOLVENCY PETITION', 'INSOLVENCY PETITION'), ('JUVENILE CALENDER CASE', 'JUVENILE CALENDER CASE'), ('LAND ACQUISITION OP', 'LAND ACQUISITION OP'), ('LAND GRABBING PETITION', 'LAND GRABBING PETITION'), ('LONG PENDING CASE', 'LONG PENDING CASE'), ('LAND REFORMS APPEAL', 'LAND REFORMS APPEAL'), ('LAND REFORMS APPEAL CASE', 'LAND REFORMS APPEAL CASE'), ('MAINTENANCE CASE', 'MAINTENANCE CASE'), ('MISC. PETITION IN ID', 'MISC. PETITION IN ID'), ('MOTOR ACCIDENT OP', 'MOTOR ACCIDENT OP'), ('ORIGINAL PETITION', 'ORIGINAL PETITION'), ('ORIGINAL SUIT', 'ORIGINAL SUIT'), ('PRE LITIGATION CASES', 'PRE LITIGATION CASES'), ('PRIMARY REGISTERED CASE', 'PRIMARY REGISTERED CASE'), ('REF. CHARGESHEET', 'REF. CHARGESHEET'), ('RENT APPEAL', 'RENT APPEAL'), ('RENT CONTROL CASE', 'RENT CONTROL CASE'), ('SESSION CASE', 'SESSION CASE'), ('SMALL CAUSE CASE', 'SMALL CAUSE CASE'), ('SESSION CASE UNDER IE ACT', 'SESSION CASE UNDER IE ACT'), ('SESSION CASE-METROPOLITAN UNIT', 'SESSION CASE-METROPOLITAN UNIT'), ('SESSIONS CASE-NDPS', 'SESSIONS CASE-NDPS'), ('Protection of Children from Sexual Offences Act', 'Protection of Children from Sexual Offences Act'), ('SESSIONS CASE-SC/ST', 'SESSIONS CASE-SC/ST'), ('SUCCESSION OP', 'SUCCESSION OP'), ('SUMMARY TRIAL CASE', 'SUMMARY TRIAL CASE'), ('TRCRLMP', 'TRCRLMP'), ('TRANSFER OP', 'TRANSFER OP')], max_length=50, null=True)),
                ('filling_number', models.IntegerField(null=True)),
                ('registration_number', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(blank=True, default=0, null=True)),
                ('case', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='case_order', to='case.case')),
                ('judge', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='permuser.judge')),
            ],
        ),
        migrations.CreateModel(
            name='Objection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scrutiny_date', models.DateField(blank=True, default=0, null=True)),
                ('objection', models.CharField(blank=True, max_length=500, null=True)),
                ('compliance_date', models.DateField(blank=True, default=0, null=True)),
                ('reciept_date', models.DateField(blank=True, default=0, null=True)),
                ('case', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='case_objection', to='case.case')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('mail_description', models.CharField(blank=True, max_length=5000, null=True)),
                ('web_description', models.CharField(blank=True, max_length=500, null=True)),
                ('is_viewed_in_mail', models.BooleanField(blank=True, default=False, null=True)),
                ('is_viewed_in_web', models.BooleanField(blank=True, default=False, null=True)),
                ('case', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='case_notifications', to='case.case')),
            ],
        ),
        migrations.CreateModel(
            name='IADetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ia_number', models.CharField(blank=True, max_length=50, null=True)),
                ('filing_date', models.DateField(blank=True, default=0, null=True)),
                ('next_date', models.DateField(blank=True, default=0, null=True)),
                ('ia_status', models.CharField(blank=True, choices=[], default='', max_length=50, null=True)),
                ('case', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='case_ia_details', to='case.case')),
                ('party', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cause_list_type', models.CharField(blank=True, max_length=50, null=True)),
                ('hearing_date', models.DateField(blank=True, default=0, null=True)),
                ('purpose_of_hearing', models.CharField(blank=True, choices=[], default='', max_length=50, null=True)),
                ('case', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='case_history', to='case.case')),
                ('judge', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='permuser.judge')),
            ],
        ),
        migrations.CreateModel(
            name='DocumentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_no', models.IntegerField(blank=True, default=0, null=True)),
                ('recieving_date', models.DateField(blank=True, default=0, null=True)),
                ('document', models.FileField(blank=True, null=True, upload_to='document/')),
                ('advocate', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='permuser.advocate')),
                ('case', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='case_document', to='case.case')),
                ('filed_by', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CaseStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_of_case', models.CharField(blank=True, max_length=50, null=True)),
                ('coram', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('bench', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('state', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('district', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('judicial', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('causelist_name', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('latest_hearing', models.DateField(blank=True, default='', null=True)),
                ('decision_date', models.DateField(blank=True, default='', null=True)),
                ('case_status', models.CharField(choices=[('PENDING', 'Pending'), ('DISPOSED', 'Disposed')], max_length=50, null=True)),
                ('next_date', models.DateField(blank=True, default='', null=True)),
                ('case', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='case_status', to='case.case')),
            ],
        ),
        migrations.CreateModel(
            name='CaseRespondent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respondent_name', models.CharField(blank=True, max_length=50, null=True)),
                ('respondent_relation', models.CharField(blank=True, max_length=50, null=True)),
                ('respondent_father', models.CharField(blank=True, max_length=50, null=True)),
                ('respondent_gender', models.CharField(blank=True, max_length=50, null=True)),
                ('respondent_address', models.TextField(blank=True, max_length=200, null=True)),
                ('respondent_country', models.CharField(blank=True, max_length=50, null=True)),
                ('petitioner_city', models.CharField(blank=True, max_length=50, null=True)),
                ('petitioner_email', models.CharField(blank=True, max_length=50, null=True)),
                ('case', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='case_respondent', to='case.case')),
            ],
        ),
        migrations.CreateModel(
            name='CasePetitioner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('petitioner_type', models.CharField(blank=True, choices=[('Arbitration Petition', 'Arbitration Petition'), ('Civil (Appeal) Petition', 'Civil (Appeal) Petition'), ('Contempt Petition (Civil)', 'Contempt Petition (Civil)'), ('Contempt Petition (Criminal)', 'Contempt Petition (Criminal)'), ('Criminal Appeal Petition', 'Criminal Appeal Petition'), ('Election Petition', 'Election Petition'), ('Original Suit', 'Original Suit'), ('Petition for Special Leave to Appeal', 'Petition for Special Leave to Appeal'), ('Transferred Case Petition', 'Transferred Case Petition'), ('Writ Petition', 'Writ Petition'), ('Review Petition', 'Review Petition'), ('Curative Petition', 'Curative Petition')], default='', max_length=50, null=True)),
                ('petitioner_name', models.CharField(blank=True, max_length=50, null=True)),
                ('petitioner_age', models.CharField(blank=True, max_length=50, null=True)),
                ('petitioner_state', models.CharField(blank=True, max_length=50, null=True)),
                ('petitioner_address', models.CharField(blank=True, max_length=200, null=True)),
                ('petitioner_country', models.CharField(blank=True, max_length=50, null=True)),
                ('petitioner_mobile', models.IntegerField(blank=True, null=True)),
                ('petitioner_department', models.CharField(blank=True, max_length=50, null=True)),
                ('petitioner_city', models.CharField(blank=True, max_length=50, null=True)),
                ('petitioner_email', models.CharField(blank=True, max_length=50, null=True)),
                ('petitioner_pin', models.IntegerField(blank=True, null=True)),
                ('petitioner_district', models.CharField(blank=True, max_length=50, null=True)),
                ('petitioner_total_petition', models.IntegerField(blank=True, null=True)),
                ('case', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='case_petitioner', to='case.case')),
            ],
        ),
        migrations.CreateModel(
            name='CaseAct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act_title', models.CharField(blank=True, max_length=150, null=True)),
                ('act_rule', models.CharField(blank=True, max_length=150, null=True)),
                ('section', models.CharField(blank=True, max_length=450, null=True)),
                ('rule_no', models.IntegerField(blank=True, null=True)),
                ('act_belong_to', models.CharField(blank=True, choices=[('CENTRAL', 'Central'), ('STATE', 'State')], max_length=50, null=True)),
                ('case', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='case_act', to='case.case')),
                ('petition', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='case_petitioner', to='petitionFiling.petition')),
            ],
        ),
    ]
