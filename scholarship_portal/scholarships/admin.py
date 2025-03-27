from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Scholarship, Application

admin.site.register(User, UserAdmin)
admin.site.register(Scholarship)
admin.site.register(Application)
