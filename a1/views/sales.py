from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from a1.models import Author
from a1.models import Book
from a1.models import Sale
from a1.serializers import AuthorSerializer
from a1.serializers import SaleSerializer
from a1.forms import AuthorForm
from django.views.generic.edit import CreateView
from django.views.generic import DeleteView
from django.http import JsonResponse
from django.shortcuts import render, redirect
from a1.models import Sale, Book
from a1.forms import SaleForm

def create_sale(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
    except Book.DoesNotExist:
        return redirect('home')

    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.book = book
            sale.save()
            return redirect(f'/book/{book_id}/sales/')
    else:
        form = SaleForm()
    return render(request, 'create_sale.html', {'form': form})

def book_sales_index(request, book_id):
    book = Book.objects.get(pk=book_id)
    sales = Sale.objects.filter(book=book)
    return render(request, 'book_sales_index.html', {'book': book, 'sales': sales})

class IndexSales(View):
    def get(self, request, book_id):
        order_by = request.GET.get('order_by', 'id')
        sales = Sale.objects.all().order_by(order_by)
        context = {
            'sales': SaleSerializer(sales, many=True).data
        }
        return render(request, 'sales.html', context)

class EditSaleView(View):
    template_name = 'edit-sale.html'
    form_class = SaleForm

    def get(self, request, sale_id):
        sale = get_object_or_404(Sale, id=sale_id)
        form = self.form_class(instance=sale)
        return render(request, self.template_name, {'form': form, 'sale': sale})

    def post(self, request, sale_id):
        sale = get_object_or_404(Sale, id=sale_id)
        form = self.form_class(request.POST, instance=sale)
        if form.is_valid():
            form.save()
            return redirect(f'/book/{sale.book.id}/sales/')
        return render(request, self.template_name, {'form': form, 'sale': sale})

def delete_sale(request, sale_id):
    try:
        sale = Sale.objects.get(id=sale_id)
        sale.delete()
        return JsonResponse({'message': 'Sale deleted successfully.'})
    except Author.DoesNotExist:
        return JsonResponse({'error': 'Sale not found.'}, status=404)
    except Exception as e:
        return JsonResponse({'error': 'Error deleting sale.'}, status=500)