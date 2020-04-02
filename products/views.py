from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .forms import ProductForm
from .models import Products
from .forms import RawproductForm
# Create your views here.


def product_list_view(request):
    queryset = Products.objects.all()
    print(queryset)
    context = {
        "object_list":  queryset
    }
    return render(request, "products/product_list.html", context)

def dynamic_lookup_view(request, id):
    try: 
        obj = Products.objects.get(id= id)
    except:
        raise Http404
        # obj = get_object_or_404(Products, id=id)
    context = {
        "object": obj
    }
    return render(request, "products/product_detail.html", context)


def product_create_view(request):
    my_form = RawproductForm()

    if request.method == 'POST':
        my_form = RawproductForm(request.POST)
        if my_form.is_valid():
            print(my_form.cleaned_data)
            Products.objects.create(**my_form.cleaned_data)
        else:
            print(my_form.errors)


    context = {
        "form" : my_form
    }
    return render(request, "products/product_create.html", context)


# def product_create_view(request):
    
#     if request.method == 'POST':
#         my_new_title = request.POST.get('title')
#         print(my_new_title)
#     context = {}
#     return render(request, "products/product_create.html", context)


# def product_create_view(request):
    
#     form = ProductForm(request.POST or None)

#     if form.is_valid():
#         form.save()
#         form = ProductForm()
#     context = {
#         'form': form
#     }
#     return render(request, "products/product_create.html", context)



def product_detail_view(request):
    obj = Products.objects.get(id = 1)
    # context = {
    #     'title' : obj.title,
    #     'description' : obj.description
    # }
    context = {
        'object': obj
    }
    return render(request, "products/product_detail.html", context)
