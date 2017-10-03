from rest_framework import serializers
from .models import DRFTest


class DRFTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DRFTest
        fields = [
            'name',
            'description'
        ]
