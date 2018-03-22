from rest_framework import serializers
from .models import Txt


class TxtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Txt
        fields = '__all__'
