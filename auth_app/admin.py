from django.contrib import admin
from .forms import FamilyDoctorForm
from .models import CustomUser, Doctor, Patient, Address, FamilyDoctor

class FamilyDoctorAdmin(admin.ModelAdmin):
  form = FamilyDoctorForm

admin.site.register(CustomUser)
admin.site.register(Doctor)
admin.site.register(Patient)

admin.site.register(FamilyDoctor, FamilyDoctorAdmin)
admin.site.register(Address)


