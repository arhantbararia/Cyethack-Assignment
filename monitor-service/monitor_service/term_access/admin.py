from django.contrib import admin
from .models import Installed_App, Running_Apps
# Register your models here.
admin.site.register(Installed_App)
admin.site.register(Running_Apps)

