# Generated by Django 4.1 on 2022-08-25 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
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
                ('court', models.CharField(blank=True, choices=[('SUPREME_COURT', 'Supreme Court'), ('HIGH-COURT', 'High Court'), ('DISTRICT_COURT', 'District Court'), ('LOWER COURT', 'Lower Court')], max_length=50, null=True)),
                ('stage_of_case', models.CharField(blank=True, max_length=50, null=True)),
                ('coram', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('bench', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('state', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('district', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('judicial', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('causelist_name', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('latest_hearing', models.DateField(blank=True, default=None, null=True)),
                ('decision_date', models.DateField(blank=True, default=None, null=True)),
                ('case_status', models.CharField(choices=[('Pending', 'Pending'), ('Disposed', 'Disposed')], max_length=50, null=True)),
                ('next_date', models.DateField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_no', models.IntegerField(blank=True, default=0, null=True)),
                ('recieving_date', models.DateField(blank=True, default=0, null=True)),
                ('document', models.FileField(blank=True, null=True, upload_to='document/')),
                ('document_type', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cause_list_type', models.CharField(blank=True, max_length=50, null=True)),
                ('hearing_date', models.DateField(blank=True, default=0, null=True)),
                ('purpose_of_hearing', models.CharField(blank=True, choices=[], default='', max_length=50, null=True)),
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
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_title', models.CharField(blank=True, max_length=250, null=True)),
                ('case_description', models.CharField(blank=True, max_length=500, null=True)),
                ('notification_date', models.DateField(blank=True, default=None, null=True)),
                ('action_date', models.DateField(blank=True, default=None, null=True)),
                ('is_notification_recieved', models.BooleanField(blank=True, default=False)),
                ('notify_type', models.CharField(blank=True, choices=[('New Case Update', 'New Case Update'), ('Doc Deadline', 'Doc Deadline'), ('Hearing Update', 'Hearing Update'), ('Next Hearing', 'Next Hearing'), ('Hearing in 2 days', 'Hearing in 2 days')], max_length=150, null=True)),
                ('action_location', models.CharField(blank=True, max_length=150, null=True)),
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
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrackCases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_status', models.CharField(blank=True, choices=[('Case Dates Updated', 'Case Dates Updated'), ('Doc Updated', 'Doc Updated')], max_length=150, null=True)),
                ('action_description', models.CharField(blank=True, max_length=250, null=True)),
                ('action_date', models.DateField(blank=True, default=None, null=True)),
            ],
        ),
    ]
