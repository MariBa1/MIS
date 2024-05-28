from django.core.exceptions import ValidationError

from datetime import date, timedelta

def validate_date_of_birth(value):
    today = date.today()
    eighty_years_ago = today - timedelta(days=80*365.25)
    if value < eighty_years_ago:
        raise ValidationError('Дата народження не може бути раніше ніж %(years)d років тому.',
                              params={'years': 80})