from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'default_phone_number', 'default_country', 'default_town_or_city')
    search_fields = ('user__username', 'default_phone_number', 'default_town_or_city')
    list_filter = ('default_country',)
    ordering = ('user',)

# Registra o modelo UserProfile no admin
admin.site.register(UserProfile, UserProfileAdmin)