from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from a1.models import Book
from a1.models import Review
from a1.serializers import ReviewSerializer
from a1.forms import ReviewForm
from django.views.generic.edit import CreateView
from django.views.generic import DeleteView
from django.http import JsonResponse
from django.views.generic import DetailView

class ReviewsView(View):
    def get(self, request, book_id):
        reviews = Review.objects.filter(book=book_id)
        book = Book.objects.get(id=book_id)
        return render(request, 'index-reviews.html', {'reviews': reviews, 'book': book})

def create_review(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return redirect('home')

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.book = book
            sale.save()
            return redirect(f'/book/{book_id}/reviews')
    else:
        form = ReviewForm()
    return render(request, 'create-reviews.html', {'form': form})


class EditReviewView(View):
    template_name = 'edit-review.html'
    form_class = ReviewForm

    def get(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        form = self.form_class(instance=review)
        return render(request, self.template_name, {'form': form, 'sale': review})

    def post(self, request, review_id):
        review = get_object_or_404(Review, id=review_id)
        form = self.form_class(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect(f'/book/{review.book.id}/reviews')
        return render(request, self.template_name, {'form': form, 'review': review})

def delete_review(request, review_id):
    try:
        review = Review.objects.get(id=review_id)
        review.delete()
        return JsonResponse({'message': 'Review deleted successfully.'})
    except Review.DoesNotExist:
        return JsonResponse({'error': 'Review not found.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': 'Error deleting review.'}, status=500)

def upvote_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.number_of_up_votes += 1
    review.save()
    return JsonResponse({'upvotes': review.number_of_up_votes})

def downvote_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.number_of_down_votes += 1
    review.save()
    return JsonResponse({'downvotes': review.number_of_down_votes})