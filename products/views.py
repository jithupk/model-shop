from django.shortcuts import render, redirect
from.models import product_list
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import product_list
from .forms import ModelForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

class productListView(ListView):
    model = product_list
    template_name = 'products/index.html'
    context_object_name = 'additem'


class ProductDetailView(DetailView):
    model= product_list
    template_name = 'products/details.html'
    context_object_name = 'product'


def add(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES.get('img')
        p = product_list(name=name, description=description, price=price, image=image)
        p.save()
        return redirect('/')
    else:
        print('someting went wrong')
    return render(request, 'products/add.html')


class ProductUpdateView(UpdateView):
    model = product_list
    template_name = 'products/edit.html'
    context_object_name = 'product'
    fields = ('name', 'description', 'price', 'image')
    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.id})


class ProductDeleteView(DeleteView):
    model = product_list
    template_name = 'products/delete.html'
    success_url = reverse_lazy('product')

# def product(request):
#     item = product_list.objects.all()
#     return render(request, 'products/index.html', {'additem': item})


    # def detail(request, product_id):
#     product1 = product_list.objects.get(id=product_id)
#     return render(request, "products/details.html", {'product': product1})


# def update(request,id):
#     product = product_list.objects.get(id=id)
#     form = ModelForm(request.POST or None, request.FILES, instance=product)
#     if form.is_valid():
#          form.save()
#          return redirect('/')
#     return render(request, 'products/edit.html', {'product':product, 'form': form})


# def delete(request,id):
#     if request.method == 'POST':
#         product = product_list.objects.get(id=id)
#         product.delete()
#         return redirect('/')
#     return render(request, 'products/delete.html')



