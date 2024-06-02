from django import template

register = template.Library()

@register.filter
def custom_yesno(value):
    if value=="Виявлено":
        return "✔"
    elif value=='Не виявлено':
        return "✘"