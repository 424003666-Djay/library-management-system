
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=150)
    isbn = models.CharField(max_length=20, unique=True)
    category = models.CharField(max_length=100)
    published_year = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title


class Borrower(models.Model):
    full_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name


class BorrowingRecord(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="borrowing_records"
    )
    borrower = models.ForeignKey(
        Borrower,
        on_delete=models.CASCADE,
        related_name="borrowing_records"
    )
    borrow_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.borrower} - {self.book}"