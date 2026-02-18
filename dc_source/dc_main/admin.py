from django.contrib import admin
from .models import Manager, Engineer, Quorom, Administrator

# Register your models here.

admin.site.register(Engineer)
admin.site.register(Manager)
admin.site.register(Quorom)
admin.site.register(Administrator)