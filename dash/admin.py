from django.contrib import admin
from dash.models import User, PasswordEntry


admin.site.register(User)
admin.site.register(PasswordEntry)
