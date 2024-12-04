from django.db import models
from authentication.models import User
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.postgres.fields.jsonb import JSONField
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Company(models.Model):
    STATUS_OPTIONS = [
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('disapproved', 'disapproved'),
    ]
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, unique=True)
    sector = models.CharField(max_length=255)
    sub_sector = models.CharField(max_length=255, null=True, blank=True)
    upload_date = models.DateField(null=True)
    status = models.CharField(choices=STATUS_OPTIONS, max_length=255, default="not started")
    uploaded_by = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, related_name='uploaded_by')
    year_of_incorporation = models.IntegerField()
    remark = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class FinancialData(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="financial_data")
    revenue = models.JSONField()  # Storing revenue by year in a JSON format
    pbt = models.JSONField()      # Storing PBT by year in a JSON format
    pat = models.JSONField()      # Storing PAT by year in a JSON format
    total_assets = models.JSONField()
    cash_equivalent = models.JSONField()
    equity = models.JSONField()
    fiscal_year_end = models.JSONField()
    
    def __str__(self):
        return f"{self.company.name}"