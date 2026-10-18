from rest_framework import serializers

from .models import Author


class AuthorSerializer(serializers.ModelSerializer):



    def validate_name(self, value):

        name = value.strip()
        if not name :
            raise serializers.ValidationError("Please enter author's name")
        return name

    def validate_email(self, value):
        email = value.strip().lower()

        if not email:
            raise serializers.ValidationError("Email is required")

        existing = Author.objects.filter(email__iexact=email).exclude(pk=self.instance.pk if self.instance else None).exists()

        if existing:
            raise serializers.ValidationError("Email already exists")
        return email



    class Meta:
        model = Author
        fields = '__all__'


