from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

from documents.utils import user_directory_path
# Create your models here.

User = get_user_model()
CHOICES = (
        ('passport', 'Passport'),
        ('id', 'ID'),
        ('bachelor', 'Bachelor'),
        ('driving_licence', 'Driving Licence'),
        ('bank_account_passbook', 'Bank Account Passbook'),
        ('telephone_bill', 'Telephone Bill'),
        ('electricity_bill', 'Electricity Bill'),
    )


class UserDocument(models.Model):
    """ Store User Documents """
    
    user = models.ForeignKey(User,related_name='documents', on_delete=models.CASCADE)
    doc_type = models.CharField(max_length=120, choices=CHOICES)
    document = models.FileField(upload_to=user_directory_path)


    def __str__(self):
        return self.doc_type


class VersionControlPloicy(models.Model):
    """ Store Version control policy for documents """ 
    ver_title =  models.CharField(max_length=120)
    policy = models.CharField(max_length=255)

    def clean(self):
        """ Ensure that admin can only input valid policy """
        doc_types = self.policy.split(',')
        choices = set([choice[0] for choice in CHOICES])
        for doc_type in doc_types:
            if doc_type not in choices:
                raise ValidationError('Invalid verification: {}'.format(doc_type))
       
    def __str__(self):
        return self.ver_title