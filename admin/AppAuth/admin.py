from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Dialect,Language
# Register your models here.

admin.site.register(Dialect)
admin.site.register(Language)