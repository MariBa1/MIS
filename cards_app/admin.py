from django.contrib import admin
from .models import MedCards, SignalMarks, IndividualMarks, Vaccination, CardVaccine, DoctorExamination


class MedCardsAdmin(admin.ModelAdmin):
  readonly_fields = ('patient', 'doctor')
  list_display = ('id','patient', 'doctor', 'dispensary_group', 'registration_date', 'deregistration_date')


admin.site.register(IndividualMarks)
admin.site.register(MedCards, MedCardsAdmin)
admin.site.register(SignalMarks)
admin.site.register(Vaccination)
admin.site.register(CardVaccine)
admin.site.register(DoctorExamination)
