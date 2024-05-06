from django.contrib import admin
from .models import CustomUser, Doctor, Patient, Address, FamilyDoctor

admin.site.register(CustomUser)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(FamilyDoctor)
admin.site.register(Address)


