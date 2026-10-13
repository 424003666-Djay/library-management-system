from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Book, Borrower, BorrowingRecord


def home(request):
    context = {
        "total_books": Book.objects.count(),
        "total_borrowers": Borrower.objects.count(),
        "total_borrowing_records": BorrowingRecord.objects.count(),
    }
    return render(request, 'library/home.html', context)


def book_list(request):
    books = Book.objects.all().order_by("title")
    return render(request, "library/book_list.html", {
        "books": books
    })


def borrower_list(request):
    borrowers = Borrower.objects.all().order_by("full_name")
    return render(request, "library/borrower_list.html", {
        "borrowers": borrowers
    })


def borrowing_record_list(request):
    records = BorrowingRecord.objects.select_related(
        "book", "borrower"
    ).all().order_by("-borrow_date")

    return render(request, "library/borrowing_record_list.html", {
        "records": records
    })


def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        author = request.POST.get("author", "").strip()
        isbn = request.POST.get("isbn", "").strip()
        category = request.POST.get("category", "").strip()
        published_year = request.POST.get("published_year", "").strip()
        quantity = request.POST.get("quantity", "1").strip()

        if not all([title, author, isbn, category, published_year, quantity]):
            messages.error(request, "Please fill in all fields.")
            return render(request, "library/add_book.html")

        try:
            published_year = int(published_year)
            quantity = int(quantity)

            if published_year < 1 or quantity < 0:
                raise ValueError

            Book.objects.create(
                title=title,
                author=author,
                isbn=isbn,
                category=category,
                published_year=published_year,
                quantity=quantity,
            )

            messages.success(request, "Book added successfully!")
            return redirect("book_list")

        except ValueError:
            messages.error(
                request,
                "Enter a valid published year and a non-negative quantity."
            )
        except Exception:
            messages.error(
                request,
                "Could not add the book. Check that the ISBN is unique."
            )

    return render(request, "library/add_book.html")


def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.title = request.POST.get("title", "").strip()
        book.author = request.POST.get("author", "").strip()
        book.isbn = request.POST.get("isbn", "").strip()
        book.category = request.POST.get("category", "").strip()
        try:
            book.published_year = int(request.POST.get("published_year"))
            book.quantity = int(request.POST.get("quantity"))
            if book.published_year < 1 or book.quantity < 0:
                raise ValueError
            book.save()
            messages.success(request, "Book updated successfully!")
            return redirect("book_list")
        except ValueError:
            messages.error(request, "Enter a valid year and quantity.")
        except Exception:
            messages.error(
                request,
                "Could not update the book. Check that the ISBN is unique."
            )
    return render(request, "library/edit_book.html", {"book": book})

def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        messages.success(request, "Book deleted successfully!")
    return redirect("book_list")

def borrow_book(request):
    if request.method == "POST":
        book_id = request.POST.get("book")
        borrower_id = request.POST.get("borrower")

        book = get_object_or_404(Book, id=book_id)
        borrower = get_object_or_404(Borrower, id=borrower_id)

        if book.quantity < 1:
            messages.error(request, "Out of stock na ang librong ito.")
            return redirect("borrowing_record_list")

        # Bawasan ng 1 ang quantity ng libro
        book.quantity -= 1
        book.save()

        # Gumawa ng borrowing record
        BorrowingRecord.objects.create(
            book=book,
            borrower=borrower,
            status="BORROWED"
        )

        messages.success(
            request, 
            f"Matagumpay na naipahiram ang '{book.title}' kay {borrower.full_name}!"
        )
        return redirect("borrowing_record_list")

    books = Book.objects.filter(quantity__gt=0)
    borrowers = Borrower.objects.all()
    return render(
        request, 
        "library/borrow_book.html", 
        {"books": books, "borrowers": borrowers}
    )

def return_book(request, record_id):
    record = get_object_or_404(BorrowingRecord, id=record_id)
    if record.status == "BORROWED":
        record.status = "RETURNED"
        record.save()

        # Dagdagan ng 1 ang available quantity ng libro
        record.book.quantity += 1
        record.book.save()

        messages.success(request, f"Matagumpay na naisauli ang '{record.book.title}'!")

    return redirect("borrowing_record_list")