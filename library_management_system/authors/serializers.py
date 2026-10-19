from rest_framework import serializers
from .models import Author


class AuthorSerializer(serializers.ModelSerializer):

    def validate_name(self, value):
        name = value.strip()

        if not name:
            raise serializers.ValidationError(
                "Author name cannot be empty."
            )

        return name

    def validate_email(self, value):
        if not value:
            return None

        email = value.strip().lower()

        if not email:
            return None

        existing = Author.objects.filter(
            email__iexact=email
        ).exclude(
            pk=self.instance.pk if self.instance else None
        ).exists()

        if existing:
            raise serializers.ValidationError(
                "An author with this email already exists."
            )

        return email

    class Meta:
        model = Author
        fields = "__all__"

