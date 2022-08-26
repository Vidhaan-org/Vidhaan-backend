# Generated by Django 4.1 on 2022-08-25 23:39

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Act',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('act_title', models.CharField(blank=True, max_length=150, null=True)),
                ('act_rule', models.CharField(blank=True, max_length=150, null=True)),
                ('section', models.CharField(blank=True, max_length=450, null=True)),
                ('rule_no', models.IntegerField(blank=True, null=True)),
                ('act_belong_to', models.CharField(blank=True, choices=[('CENTRAL', 'Central'), ('STATE', 'State')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Judge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judge_name', models.CharField(blank=True, max_length=50, null=True)),
                ('judge_number', models.IntegerField(blank=True, null=True)),
                ('judge_year', models.IntegerField(blank=True, null=True)),
                ('judge_mobile', models.IntegerField(blank=True, null=True)),
                ('judge_email_id', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonInvolved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_name', models.CharField(blank=True, max_length=50, null=True)),
                ('person_mobile', models.IntegerField(blank=True, null=True)),
                ('person_email', models.CharField(blank=True, max_length=50, null=True)),
                ('person_age', models.CharField(blank=True, max_length=50, null=True)),
                ('person_address', models.CharField(blank=True, max_length=200, null=True)),
                ('person_state', models.CharField(blank=True, max_length=50, null=True)),
                ('person_city', models.CharField(blank=True, max_length=50, null=True)),
                ('person_pin', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Petitioner',
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
            ],
        ),
        migrations.CreateModel(
            name='Respondent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respondent_name', models.CharField(blank=True, max_length=50, null=True)),
                ('respondent_relation', models.CharField(blank=True, max_length=50, null=True)),
                ('respondent_father', models.CharField(blank=True, max_length=50, null=True)),
                ('respondent_gender', models.CharField(blank=True, max_length=50, null=True)),
                ('respondent_address', models.TextField(blank=True, max_length=200, null=True)),
                ('respondent_country', models.CharField(blank=True, max_length=50, null=True)),
                ('respondent_city', models.CharField(blank=True, max_length=50, null=True)),
                ('respondent_email', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TabPermission',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UGCExecutive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('executive_name', models.CharField(blank=True, max_length=50, null=True)),
                ('executive_mobile', models.IntegerField(blank=True, null=True)),
                ('executive_email', models.CharField(blank=True, max_length=50, null=True)),
                ('executive_age', models.CharField(blank=True, max_length=50, null=True)),
                ('executive_address', models.CharField(blank=True, max_length=200, null=True)),
                ('executive_state', models.CharField(blank=True, max_length=50, null=True)),
                ('executive_city', models.CharField(blank=True, max_length=50, null=True)),
                ('executive_pin', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Advocate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advocate_name', models.CharField(blank=True, max_length=50, null=True)),
                ('advocate_year', models.IntegerField(blank=True, null=True)),
                ('advocate_mobile', models.IntegerField(blank=True, null=True)),
                ('advocate_email_id', models.CharField(blank=True, max_length=50, null=True)),
                ('advocate_type', models.CharField(blank=True, choices=[('PETITIONER_ADVOCATE', 'Petitioner Advocate'), ('RESPONDENT_ADVOCATE', 'Respondent Advocate')], max_length=50, null=True)),
                ('advocate_expertise', models.ManyToManyField(blank=True, null=True, to='permuser.tags')),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(blank=True, choices=[('Super Admin', 'Super Admin'), ('Advocate', 'Advocate'), ('UGC Executive', 'UGC Executive')], default='', max_length=50, null=True)),
                ('name', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('expertise', models.ManyToManyField(blank=True, null=True, to='permuser.tags')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('tab_permission', models.ManyToManyField(blank=True, default='', related_name='user_permission', to='permuser.tabpermission')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
