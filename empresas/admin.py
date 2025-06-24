from django.contrib import admin
from empresas.models import Empresas
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Empresas,ImportExportModelAdmin)