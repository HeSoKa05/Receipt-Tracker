from django.contrib import admin
from .models import ReceiptModel


class ReceiptModelAdmin(admin.ModelAdmin):
    """
    register the ReceiptModel model in the admin panel,
    and define the fields to be shown
    """
    fields = [
        'store_name',
        'purchase_date',
        'item_list',
        'total_amount'
    ]

    class Meta:
        model = ReceiptModel


admin.site.register(ReceiptModel, ReceiptModelAdmin)
