from django.contrib import admin

from testalmikeev.models import GoogleTab, FileCsv, Report


@admin.register(GoogleTab)
class GoogleTabAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'last_change_date', 'total_price', 'discount_percent', 'warehouse_name', 'oblast', 'nm_id', 'category', 'brand', 'is_cancel', 'cancel_dt', 'created_at', 'updated_at', 'order_type']


@admin.register(FileCsv)
class FileCsvAdmin(admin.ModelAdmin):
    list_display = ['id', 'file']


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'nm_id', 'report']
