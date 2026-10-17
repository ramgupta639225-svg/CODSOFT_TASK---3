from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):

    def validate_title(self, value):
        title = value.strip()

        if not title:
            raise serializers.ValidationError('Book title cannot be empty')

        existing = Book.objects.filter(title__icontains=title).exclude(pk=self.instance if self.instance else None).exists()

        if existing:
            raise serializers.ValidationError('Book title already exists')
        return title



    def validate_isbn(self, value):
        isbn = value.strip()

        existing = Book.objects.filter(isbn=isbn).exclude(pk=self.instance.pk if self.instance else None).exists()
        if existing:
            raise serializers.ValidationError('Book isbn already exists')
        return isbn


    def validate_category(self, value):
        category = value.strip()
        if not category:
            raise serializers.ValidationError('Book category cannot be empty')
        return category



    def validate(self, data):

        total_copies = data.get('total_copies', self.instance.total_copies if self.instance else 1)


        available_copies = data.get('available_copies', self.instance.available_copies if self.instance else 1)

        if available_copies > total_copies:
            raise serializers.ValidationError({
                'available_copies': 'Available copies cannot exceed total copies.'
            })

        return data



    class Meta:
        model = Book
        fields = '__all__'



