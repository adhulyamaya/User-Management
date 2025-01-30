from django.contrib import admin
from .models import MainAdmin,CustomUser,Staff
# Register your models here.
admin.site.register(MainAdmin)
admin.site.register(CustomUser)
admin.site.register(Staff)
