from rest_framework import serializers
from core.models import Quotes

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Quotes
        fields=(
            'id',
            'name',
            'phone',
            'email',
            'address',
            'zip_code'
        )