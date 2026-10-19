from django.db import transaction
from django.utils import timezone

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import IssuedBook
from .serializers import IssuedBookSerializer
from books.models import Book


class IssuedBookViewSet(viewsets.ModelViewSet):
    queryset = IssuedBook.objects.select_related(
        "book",
        "member"
    ).all()

    serializer_class = IssuedBookSerializer

    @action(detail=True, methods=["post"], url_path="return")
    def return_book(self, request, pk=None):
        with transaction.atomic():
            issued_book = IssuedBook.objects.select_for_update().filter(
                pk=pk
            ).first()

            if issued_book is None:
                return Response(
                    {"error": "Issued book record not found."},
                    status=status.HTTP_404_NOT_FOUND
                )

            if issued_book.status == "returned":
                return Response(
                    {"error": "This book has already been returned."},
                    status=status.HTTP_400_BAD_REQUEST
                )

            book = Book.objects.select_for_update().get(
                pk=issued_book.book_id
            )

            if book.available_copies >= book.total_copies:
                return Response(
                    {
                        "error": (
                            "Book inventory is inconsistent. "
                            "Please check available copies."
                        )
                    },
                    status=status.HTTP_409_CONFLICT
                )

            issued_book.status = "returned"
            issued_book.return_date = timezone.localdate()
            issued_book.save(
                update_fields=["status", "return_date", "updated_date"]
            )

            book.available_copies += 1
            book.save(update_fields=["available_copies"])

            response_data = {
                "message": "Book returned successfully.",
                "issued_book_id": issued_book.id,
                "book": book.title,
                "return_date": issued_book.return_date,
                "available_copies": book.available_copies,
            }

        return Response(
            response_data,
            status=status.HTTP_200_OK
        )