from django.contrib import admin
from .models import Suggestion, Recipient


@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    fields = ['suggestion', 'recipient', 'status']
    list_display = ['id', 'suggestion_start', 'created', 'recipient', 'status']

    def suggestion_start(self, obj):
        return obj.suggestion[:10]
    suggestion_start.short_description = "Suggestion"
    suggestion_start.admin_order_field = "suggestion"
    ordering = ['id']


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    fields = ['name', 'email']

