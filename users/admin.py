from django.contrib import admin

from users.models import Users, Payment

admin.site.register(Payment)
admin.site.register(Users)