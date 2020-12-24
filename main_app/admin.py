from django.contrib import admin
# Import models here
from .models import Style, Wearing

# Register your models here.
admin.site.register(Style)
admin.site.register(Wearing)
