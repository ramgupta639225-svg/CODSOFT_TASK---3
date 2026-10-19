from django.db import transaction
from django.utils import timezone
from rest_framework import serializers

from .models import IssuedBook
from books.models import Book


class IssuedBookSerializer(serializers.ModelSerializer):

    def validate(self, data):
        instance = self.instance

        book = data.get(
            "book",
            instance.book if instance else None
        )

        member = data.get(
            "member",
            instance.member if instance else None
        )

        due_date = data.get(
            "due_date",
            instance.due_date if instance else None
        )

        if instance:
            if "book" in data and data["book"] != instance.book:
                raise serializers.ValidationError({
                    "book": "The book cannot be changed after issuing."
                })

            if "member" in data and data["member"] != instance.member:
                raise serializers.ValidationError({
                    "member": "The member cannot be changed after issuing."
                })

        if due_date and due_date < timezone.localdate():
            raise serializers.ValidationError({
                "due_date": "Due date cannot be in the past."
            })

        if due_date and instance and due_date < instance.issue_date:
            raise serializers.ValidationError({
                "due_date": "Due date cannot be before the issue date."
            })

        if member and not member.is_active:
            raise serializers.ValidationError({
                "member": "This member is not active."
            })

        if book and member and not instance:
            already_issued = IssuedBook.objects.filter(
                book=book,
                member=member,
                status="issued"
            ).exists()

            if already_issued:
                raise serializers.ValidationError({
                    "member": "This member has already issued this book."
                })

            if book.available_copies <= 0:
                raise serializers.ValidationError({
                    "book": "This book is not available."
                })

        return data

    def create(self, validated_data):
        with transaction.atomic():
            book = Book.objects.select_for_update().get(
                pk=validated_data["book"].pk
            )

            member = validated_data["member"]

            if not member.is_active:
                raise serializers.ValidationError({
                    "member": "This member is not active."
                })

            already_issued = IssuedBook.objects.filter(
                book=book,
                member=member,
                status="issued"
            ).exists()

            if already_issued:
                raise serializers.ValidationError({
                    "member": "This member has already issued this book."
                })

            if book.available_copies <= 0:
                raise serializers.ValidationError({
                    "book": "No copies of this book are available."
                })

            book.available_copies -= 1
            book.save(update_fields=["available_copies"])

            return IssuedBook.objects.create(**validated_data)

    class Meta:
        model = IssuedBook
        fields = "__all__"
        read_only_fields = (
            "issue_date",
            "return_date",
            "status",
            "created_date",
            "updated_date",
        )