# In a file, e.g., custom_json_encoder.py
from django.core.serializers.json import DjangoJSONEncoder
from decimal import Decimal

class CustomJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)  # Convert Decimal to string
        return super().default(obj) 