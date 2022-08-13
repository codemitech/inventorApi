from django.contrib import admin
from .models import User,inventions, investment


admin.site.register(User)
admin.site.register(inventions)
admin.site.register(investment)
# Register your models here.
