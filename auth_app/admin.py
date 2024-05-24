from django.contrib import admin
from .forms import FamilyDoctorForm, PatientForm, DoctorForm
from .models import CustomUser, Doctor, Patient, FamilyDoctor

class FamilyDoctorAdmin(admin.ModelAdmin):
  form = FamilyDoctorForm

# class PatientAdmin(admin.ModelAdmin):
#   form=PatientForm

# class DoctorAdmin(admin.ModelAdmin):
#   form=DoctorForm

admin.site.register(CustomUser)
admin.site.register(Doctor)
admin.site.register(Patient)

admin.site.register(FamilyDoctor, FamilyDoctorAdmin)
# admin.site.register(Address)


