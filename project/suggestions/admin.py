from django.contrib import admin
from .models import Suggestion, Recipient

admin.site.site_header = "Suggestion Box Django Admin"
admin.site.site_title = 'Administration'

@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    fields = ['suggestion', 'recipient', 'created', 'status', 'status_changed']
    readonly_fields = ['created', 'status_changed']
    list_display = ['id', 'suggestion_start', 'created', 'recipient', 'status']

    def suggestion_start(self, obj):
        return obj.suggestion[:10]
    suggestion_start.short_description = "Suggestion"
    suggestion_start.admin_order_field = "suggestion"
    ordering = ['id']


@admin.register(Recipient)
class RecipientAdmin(admin.ModelAdmin):
    fields = ['name', 'email']
    list_display = ['name', 'email']

