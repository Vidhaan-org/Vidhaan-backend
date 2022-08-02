from django.db import models
from pkg_resources import require

# Create your models here.
# Cnr_number
# case_type
# filling_number
# registration_number
# fiiling_date
# registration_number
# First Hearing Date
# latest_hearing
# Decision Date
# Case Status
# Nature of Disposal
# Coram
# Bench
# Judicial
# Petitioner
# P. Advocate
# Respondent
# R. Advocate
# Judge(s)
# Acts
# Section
# Next Date
# history_of_case_hearing

CASE_STATUS = (
    ('PENDING', 'PENDING'),
    ('DISPOSED', 'DISPOSED')
)
class CaseDetails(models.Model):
    cnr_number=models.IntegerField(unique=True, null=False)
    case_type=models.CharField(max_length=50, null=True)
    filling_number=models.IntegerField(null=False)
    registration_number=models.IntegerField(null=False)
    filling_date=models.DateField(null=True)
    first_hearing_date=models.DateField(null=True)
    latest_hearing=models.DateField(null=True)
    decision_date=models.DateField(null=True)
    case_status=models.CharField(max_length=50, null=False, choices=CASE_STATUS)
    coram=models.CharField(max_length=50, null=False, blank=True)
    bench=models.CharField(max_length=50, null=True)
    judicial=models.CharField(max_length=50, null=True)
    petitioner=models.CharField(max_length=50, null=True)
    p_advocate=models.CharField(max_length=50, null=True)
    respondent=models.CharField(max_length=50, null=True)
    r_advocate=models.CharField(max_length=50, null=True)
    judge=models.CharField(max_length=50, null=True)
    acts=models.CharField(max_length=50, null=True)
    section=models.CharField(max_length=50, null=True)
    next_date=models.DateField(null=True)
    history_of_case_hearing=models.TextField(null=True)
    def __str__(self):
        return str(self.cnr_number)


