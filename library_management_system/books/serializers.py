from rest_framework import serializers
from .models import Book



class BookSerializer(serializers.ModelSerializer):
    def validate_title(self, value):
        title = value.strip()
        if not title:
            raise serializers.ValidationError("Book title cannot be empty.")
        return title

    def validate_isbn(self, value):
        isbn = value.strip()
        if not isbn:
            raise serializers.ValidationError("ISBN cannot be empty.")
        if Book.objects.filter(isbn=isbn).exclude(
            pk=self.instance.pk if self.instance else None).exists():
            raise serializers.ValidationError("A book with this ISBN already exists.")
        return isbn

    def validate_category(self, value):
        category = value.strip()
        if not category:
            raise serializers.ValidationError("Book category cannot be empty.")
        return category

    def validate(self, data):
        instance = self.instance
        total_copies = data.get("total_copies", instance.total_copies if instance else 1)
        available_copies = data.get("available_copies", instance.available_copies if instance else 1)

        if total_copies < 1:
            raise serializers.ValidationError({"total_copies": "Total copies must be at least 1."})

        if available_copies > total_copies:
            raise serializers.ValidationError({"available_copies": "Available copies cannot exceed total copies."})

        if instance:
            issued_copies = instance.issued_history.filter(status="issued").count()
            if total_copies < issued_copies:
                raise serializers.ValidationError({"total_copies": f"At least {issued_copies} copies are currently issued."})

            if "total_copies" in data and "available_copies" not in data:
                total_difference = total_copies - instance.total_copies
                available_copies = instance.available_copies + total_difference

                if available_copies < 0:
                    raise serializers.ValidationError({"total_copies": "Total copies cannot be reduced below the number of issued copies."})

                data["available_copies"] = available_copies
        return data

    class Meta:
        model = Book
        fields = "__all__"
        read_only_fields = ("available_copies",)

