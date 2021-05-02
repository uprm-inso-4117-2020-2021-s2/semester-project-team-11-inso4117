from django.contrib import admin
from .models import User,Lawyer,Client
# Register your models here.

admin.site.register(User)
admin.site.register(Lawyer)
admin.site.register(Client)