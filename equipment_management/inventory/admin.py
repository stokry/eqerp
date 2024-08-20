from django.contrib import admin
from .models import Employee, Equipment

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user',)

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'assigned_to', 'issued_date')
    list_filter = ('assigned_to',)