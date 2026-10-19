from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.ModelSerializer):

    def validate_name(self, value):
        name = value.strip()

        if not name:
            raise serializers.ValidationError(
                "Member name cannot be empty."
            )

        return name

    def validate_email(self, value):
        email = value.strip().lower()

        if not email:
            raise serializers.ValidationError(
                "Email cannot be empty."
            )

        return email

    def validate_phone(self, value):
        phone = value.strip()

        if not phone:
            raise serializers.ValidationError(
                "Phone number cannot be empty."
            )

        if not phone.isdigit():
            raise serializers.ValidationError(
                "Phone number must contain digits only."
            )

        if not 10 <= len(phone) <= 13:
            raise serializers.ValidationError(
                "Phone number must contain between 10 and 13 digits."
            )

        return phone

    class Meta:
        model = Member
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")