from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CaseCase(models.Model):
    cnr_number = models.IntegerField(unique=True, blank=True, null=True)
    case_type = models.CharField(max_length=50, blank=True, null=True)
    filling_number = models.IntegerField(blank=True, null=True)
    registration_number = models.IntegerField(blank=True, null=True)
    bench = models.CharField(max_length=50, blank=True, null=True)
    causelist_name = models.CharField(max_length=50, blank=True, null=True)
    coram = models.CharField(max_length=50, blank=True, null=True)
    decision_date = models.DateField(blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    judicial = models.CharField(max_length=50, blank=True, null=True)
    latest_hearing = models.DateField(blank=True, null=True)
    next_date = models.DateField(blank=True, null=True)
    stage_of_case = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    case_status = models.CharField(max_length=50, blank=True, null=True)
    court = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'case_case'


class CaseCaseAct(models.Model):
    case = models.ForeignKey(CaseCase, models.DO_NOTHING)
    act = models.ForeignKey('PermuserAct', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'case_case_act'
        unique_together = (('case', 'act'),)


class CaseCaseAdvocate(models.Model):
    case = models.ForeignKey(CaseCase, models.DO_NOTHING)
    advocate = models.ForeignKey('PermuserAdvocate', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'case_case_advocate'
        unique_together = (('case', 'advocate'),)


class CaseCaseDocument(models.Model):
    case = models.ForeignKey(CaseCase, models.DO_NOTHING)
    documentdetails = models.ForeignKey('CaseDocumentdetails', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'case_case_document'
        unique_together = (('case', 'documentdetails'),)


class CaseCaseHistory(models.Model):
    case = models.ForeignKey(CaseCase, models.DO_NOTHING)
    history = models.ForeignKey('CaseHistory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'case_case_history'
        unique_together = (('case', 'history'),)


class CaseCaseIa(models.Model):
    case = models.ForeignKey(CaseCase, models.DO_NOTHING)
    iadetails = models.ForeignKey('CaseIadetails', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'case_case_ia'
        unique_together = (('case', 'iadetails'),)


class CaseCaseObjection(models.Model):
    case = models.ForeignKey(CaseCase, models.DO_NOTHING)
    objection = models.ForeignKey('CaseObjection', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'case_case_objection'
        unique_together = (('case', 'objection'),)


class CaseCaseOrder(models.Model):
    case = models.ForeignKey(CaseCase, models.DO_NOTHING)
    order = models.ForeignKey('CaseOrder', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'case_case_order'
        unique_together = (('case', 'order'),)


class CaseCasePersonInvolved(models.Model):
    case = models.ForeignKey(CaseCase, models.DO_NOTHING)
    personinvolved = models.ForeignKey('PermuserPersoninvolved', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'case_case_person_involved'
        unique_together = (('case', 'personinvolved'),)


class CaseCasePetitioner(models.Model):
    case = models.ForeignKey(CaseCase, models.DO_NOTHING)
    petitioner = models.ForeignKey('PermuserPetitioner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'case_case_petitioner'
        unique_together = (('case', 'petitioner'),)


class CaseCaseRespondent(models.Model):
    case = models.ForeignKey(CaseCase, models.DO_NOTHING)
    respondent = models.ForeignKey('PermuserRespondent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'case_case_respondent'
        unique_together = (('case', 'respondent'),)


class CaseDocumentdetails(models.Model):
    document_no = models.IntegerField(blank=True, null=True)
    recieving_date = models.DateField(blank=True, null=True)
    document = models.CharField(max_length=100, blank=True, null=True)
    advocate = models.ForeignKey('PermuserAdvocate', models.DO_NOTHING, blank=True, null=True)
    filed_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    document_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'case_documentdetails'


class CaseHistory(models.Model):
    cause_list_type = models.CharField(max_length=50, blank=True, null=True)
    hearing_date = models.DateField(blank=True, null=True)
    purpose_of_hearing = models.CharField(max_length=50, blank=True, null=True)
    judge = models.ForeignKey('PermuserJudge', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'case_history'


class CaseIadetails(models.Model):
    ia_number = models.CharField(max_length=50, blank=True, null=True)
    filing_date = models.DateField(blank=True, null=True)
    next_date = models.DateField(blank=True, null=True)
    ia_status = models.CharField(max_length=50, blank=True, null=True)
    party = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'case_iadetails'


class CaseNotification(models.Model):
    case_description = models.CharField(max_length=500, blank=True, null=True)
    case_title = models.CharField(max_length=250, blank=True, null=True)
    action_date = models.DateField(blank=True, null=True)
    is_notification_recieved = models.BooleanField()
    notification_date = models.DateField(blank=True, null=True)
    notify_type = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'case_notification'


class CaseNotificationCase(models.Model):
    notification = models.ForeignKey(CaseNotification, models.DO_NOTHING)
    case = models.ForeignKey(CaseCase, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'case_notification_case'
        unique_together = (('notification', 'case'),)


class CaseNotificationNotifyTo(models.Model):
    notification = models.ForeignKey(CaseNotification, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'case_notification_notify_to'
        unique_together = (('notification', 'user'),)


class CaseObjection(models.Model):
    scrutiny_date = models.DateField(blank=True, null=True)
    objection = models.CharField(max_length=500, blank=True, null=True)
    compliance_date = models.DateField(blank=True, null=True)
    reciept_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'case_objection'


class CaseOrder(models.Model):
    order_date = models.DateField(blank=True, null=True)
    judge = models.ForeignKey('PermuserJudge', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'case_order'


class CaseTrackcases(models.Model):
    action_status = models.CharField(max_length=150, blank=True, null=True)
    action_description = models.CharField(max_length=250, blank=True, null=True)
    action_date = models.DateField(blank=True, null=True)
    case = models.ForeignKey(CaseCase, models.DO_NOTHING, blank=True, null=True)
    action_taken_by = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'case_trackcases'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PermuserAct(models.Model):
    act_title = models.CharField(max_length=150, blank=True, null=True)
    act_rule = models.CharField(max_length=150, blank=True, null=True)
    section = models.CharField(max_length=450, blank=True, null=True)
    rule_no = models.IntegerField(blank=True, null=True)
    act_belong_to = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permuser_act'


class PermuserAdvocate(models.Model):
    advocate_name = models.CharField(max_length=50, blank=True, null=True)
    advocate_number = models.IntegerField(blank=True, null=True)
    advocate_year = models.IntegerField(blank=True, null=True)
    advocate_mobile = models.IntegerField(blank=True, null=True)
    advocate_email_id = models.CharField(max_length=50, blank=True, null=True)
    advocate_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permuser_advocate'


class PermuserEmployeemodel(models.Model):
    employee_name = models.TextField(blank=True, null=True)
    employee_email = models.CharField(unique=True, max_length=200)
    employee_mobile = models.CharField(unique=True, max_length=200)
    employee_password = models.CharField(unique=True, max_length=200)
    organization_permission = models.ForeignKey('PermuserUserpermission', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permuser_employeemodel'


class PermuserEmployeemodelPermissions(models.Model):
    employeemodel = models.ForeignKey(PermuserEmployeemodel, models.DO_NOTHING)
    userpermission = models.ForeignKey('PermuserUserpermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'permuser_employeemodel_permissions'
        unique_together = (('employeemodel', 'userpermission'),)


class PermuserJudge(models.Model):
    judge_name = models.CharField(max_length=50, blank=True, null=True)
    judge_number = models.IntegerField(blank=True, null=True)
    judge_year = models.IntegerField(blank=True, null=True)
    judge_mobile = models.IntegerField(blank=True, null=True)
    judge_email_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permuser_judge'


class PermuserPersoninvolved(models.Model):
    person_name = models.CharField(max_length=50, blank=True, null=True)
    person_mobile = models.IntegerField(blank=True, null=True)
    person_email = models.CharField(max_length=50, blank=True, null=True)
    person_age = models.CharField(max_length=50, blank=True, null=True)
    person_address = models.CharField(max_length=200, blank=True, null=True)
    person_state = models.CharField(max_length=50, blank=True, null=True)
    person_city = models.CharField(max_length=50, blank=True, null=True)
    person_pin = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permuser_personinvolved'


class PermuserPetitioner(models.Model):
    petitioner_type = models.CharField(max_length=50, blank=True, null=True)
    petitioner_name = models.CharField(max_length=50, blank=True, null=True)
    petitioner_age = models.CharField(max_length=50, blank=True, null=True)
    petitioner_state = models.CharField(max_length=50, blank=True, null=True)
    petitioner_address = models.CharField(max_length=200, blank=True, null=True)
    petitioner_country = models.CharField(max_length=50, blank=True, null=True)
    petitioner_mobile = models.IntegerField(blank=True, null=True)
    petitioner_department = models.CharField(max_length=50, blank=True, null=True)
    petitioner_city = models.CharField(max_length=50, blank=True, null=True)
    petitioner_email = models.CharField(max_length=50, blank=True, null=True)
    petitioner_pin = models.IntegerField(blank=True, null=True)
    petitioner_district = models.CharField(max_length=50, blank=True, null=True)
    petitioner_total_petition = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permuser_petitioner'


class PermuserRespondent(models.Model):
    respondent_name = models.CharField(max_length=50, blank=True, null=True)
    respondent_relation = models.CharField(max_length=50, blank=True, null=True)
    respondent_father = models.CharField(max_length=50, blank=True, null=True)
    respondent_gender = models.CharField(max_length=50, blank=True, null=True)
    respondent_address = models.TextField(blank=True, null=True)
    respondent_country = models.CharField(max_length=50, blank=True, null=True)
    respondent_city = models.CharField(max_length=50, blank=True, null=True)
    respondent_email = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permuser_respondent'


class PermuserUserpermission(models.Model):
    name = models.CharField(unique=True, max_length=100)
    can_edit = models.BooleanField()
    can_upload = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'permuser_userpermission'


class PetitionfilingPetition(models.Model):
    court = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    case_category = models.CharField(max_length=500, blank=True, null=True)
    special_category = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    case_type = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'petitionFiling_petition'


class PetitionfilingPetitionAct(models.Model):
    petition = models.ForeignKey(PetitionfilingPetition, models.DO_NOTHING)
    act = models.ForeignKey(PermuserAct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'petitionFiling_petition_act'
        unique_together = (('petition', 'act'),)


class PetitionfilingPetitionPetitioner(models.Model):
    petition = models.ForeignKey(PetitionfilingPetition, models.DO_NOTHING)
    petitioner = models.ForeignKey(PermuserPetitioner, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'petitionFiling_petition_petitioner'
        unique_together = (('petition', 'petitioner'),)


class PetitionfilingPetitionRespondent(models.Model):
    petition = models.ForeignKey(PetitionfilingPetition, models.DO_NOTHING)
    respondent = models.ForeignKey(PermuserRespondent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'petitionFiling_petition_respondent'
        unique_together = (('petition', 'respondent'),)
