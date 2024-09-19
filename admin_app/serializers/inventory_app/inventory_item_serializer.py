from rest_framework import serializers
from admin_app.models import PencilBoxLocationInventoryItem


class PencilBoxLocationInventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PencilBoxLocationInventoryItem
        fields = ['inventory_item','pencil_box_location', 'bin_number','low_stock','max_amt','sold','in_stock','last_audited','archived']
