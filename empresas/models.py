from django.db import models

# Create your models here.

class Empresas(models.Model):
    company_name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    sector = models.CharField(max_length=200)
    near_term_status = models.CharField(max_length=100)
    near_term_target_year = models.CharField(max_length=100)
    def __str__(self):
        return self.company_name