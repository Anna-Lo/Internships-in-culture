from django.contrib import admin
from intern_app.models import Institution, Offer


# Register your models here.
@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'province']

@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ['name', 'institution']
