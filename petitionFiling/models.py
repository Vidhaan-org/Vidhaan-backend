from django.db import models

Court = (
    ('SUPREME_COURT', 'Supreme Court'),
    ('HIGH-COURT', 'High Court'),
    ('DISTRICT_COURT', 'District Court'),
)



class Petition(models.Model):
    court=models.CharField(null=False, max_length=50, choices=Court)
    state=models.CharField(max_length=50, null=False)
    bench=models.CharField(null=False, max_length=50)
    case_type=models.CharField(null=False, max_length=50)
    special_type=models.CharField(null=False, max_length=50)

class Petitioner(models.Model):
    petitioner_type = models.CharField(null=False, max_length=50)
    petitioner_state = models.CharField(null=False, max_length=50)
    petitioner_address = models.CharField(null=False, max_length=200)
    petitioner_country = models.CharField(null=False, max_length=50)
    petitioner_mobile = models.IntegerField(null=False)
    petitioner_department = models.CharField(null=False, max_length=50)
    petitioner_city = models.CharField(null=False, max_length=50)
    petitioner_email = models.CharField(null=False, max_length=50)
    petitioner_pin = models.IntegerField(null=False, max_length=6)
    petitioner_district = models.CharField(null=False, max_length=50)
    petitioner_total_petition = models.IntegerField(null=False)
class Responded(models.Model):
    respondent_name = models.CharField(null=False, max_length=50)
    respondent_relation = models.CharField(null=False, max_length=50)
    respondent_father_husband = models.CharField(null=False, max_length=50)
    respondent_gender = models.CharField(null=False, max_length=50)
    respondent_address = models.TextField(null=False, max_length= 200)
    respondent_country = models.CharField(null=False, max_length=50)

class advocate:
    advocate_name = models.CharField(null=False, max_length=50)
    advocate_number = models.IntegerField(null=False)
    advocate_year = models.IntegerField(null=False)
    advocate_mobile = models.IntegerField(null=False)
    advocate_email_id = models.CharField(null=False, max_length=50)

