from django.db import models

from library_management_system.books.models import Book


# Create your models here.


class IssuedBook(models.Model):


    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name='issued_history')
    member = models.ForeignKey('members.Member', on_delete=models.PROTECT, related_name='borrow_history')
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=[('issued', 'Issued'), ('returned', 'Returned')], default='issued')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.book.title} - {self.member.name}"
