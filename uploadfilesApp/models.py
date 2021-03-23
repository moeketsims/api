from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Upload(models.Model):

    class SourceFile(models.TextChoices):
        sas    = 'Student Academic Support'
        career = 'Career Path'
        qa     = 'Quality Assurance'
        elearn = 'E-Learning'

    owner       = models.ForeignKey(to = User, on_delete=models.CASCADE)
    source      = models.CharField(max_length=100, choices=SourceFile.choices)
    descprition = models.TextField()
    created_at  = models.DateField(auto_now_add=True)
    updated_at  = models.DateField(auto_now=True)
    docx = models.FileField(upload_to='documents/files')
    is_UCDP     = models.BooleanField(default=False)
    