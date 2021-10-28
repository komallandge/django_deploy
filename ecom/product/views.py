from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from product.models import Product
from django.http import HttpResponse
from product.forms import ProductForm


# Create your views here.
def get_product(id):
    return Product.Objects.get(pk=id)


def get_products(request):
    all_products = Product.objects.all()
    if all_products:
        return render(request, 'index.html', {"msg": "Welcome", "all_products": all_products})
    return request(request, 'index.html', {"msg": "No data in records", "all_products": []})


def create_product(request):
    try:

        prod = get_product(request.POST["pid"])
    except MultiValueDictKeyError:
        prod = None

    if prod:
        form = ProductForm(request.POST, instance=prod)
        msg: "Product Updated"
    else:
        form = ProductForm(request.POST)
        msg: "Product Created"

    if request.method == "POST":
        if form.is_valid():
            form.save()
            return render(request, 'index.html', {"msg": msg, "all_products": Product})
        else:
            return render(request, 'edit.html', {"msg": "form.errors", 'form': form})
    return render(request, 'edit.html', {"msg": "please fill following data", 'form': form})


def update_product(request, id):
    prod = get_product(id)
    if prod:
        form = ProductForm(instance=prod)
        return render(request, 'edit.html', {"form": form})
    return redirect('get_all')


def delete_product(request, id):
    msg = "Product Not Found"
    prod = get_product(id)
    if prod:
        prod.delete()
        msg = "Product Deleted"
    return render(request, 'index.html', {"msg": msg, 'all_products': Product.objects.all()})
