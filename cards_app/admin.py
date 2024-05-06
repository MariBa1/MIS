from django.contrib import admin
from .models import MedCards, SignalMarks, IndividualMarks, Vaccination, CardVaccine, DoctorExamination


admin.site.register(IndividualMarks)
admin.site.register(MedCards)
admin.site.register(SignalMarks)
admin.site.register(Vaccination)
admin.site.register(CardVaccine)
admin.site.register(DoctorExamination)

