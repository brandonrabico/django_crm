from django.contrib import admin
from .models import CustomUser, Lead, Agent, UserProfile, Category
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Lead)
admin.site.register(Agent)
admin.site.register(UserProfile)
admin.site.register(Category)