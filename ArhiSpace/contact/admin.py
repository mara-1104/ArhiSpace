from django.contrib import admin
from .models import ContactMessage

# Register your models here.

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sent_at')
    readonly_fields = ('name', 'email', 'message', 'sent_at')
    ordering = ('-sent_at',)