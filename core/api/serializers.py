from rest_framework import serializers
from core.models import Quotes,Contact

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

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields=(
            'id',
            'first_name',
            'last_name',
            'phone',
            'email',
            'message',
        )