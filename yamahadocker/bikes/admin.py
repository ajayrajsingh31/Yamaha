from django.contrib import admin
from .models import BikeModel

# Register your models here.
class BikeAdmin(admin.ModelAdmin):
    list_display = ['bikename']

# Register the BikeModel with the admin site
admin.site.register(BikeModel, BikeAdmin)
