from rest_framework import serializers

from .models import IssuedBook


class IssuedBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssuedBook
        fields = '__all__'

