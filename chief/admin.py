from django.contrib import admin
from chief.models import Therapist,Patient,Problem,Solution
# Register your models here.


class TherapistAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'request_status', 'therapist_id', 'user')
    
admin.site.register(Therapist, TherapistAdmin)

class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient_id', 'name', 'contact_number', 'user')
    
admin.site.register(Patient, PatientAdmin)

admin.site.register(Problem)

admin.site.register(Solution)

admin.site.site_header = 'HOPE ADMINISTRATION'  # set header
admin.site.site_title = 'HOPE ADMINISTRATION'   # set title
admin.site.index_title = 'HOPE ADMINISTRATION'