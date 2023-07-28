from django.shortcuts import render
from.forms import ProductAploadForm
from inventory.models import Product



# Create your views here.
def upload_product(request):
    if request.method == "POST":
        form = ProductAploadForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()


    else:
        form = ProductAploadForm()
    return render(request,"inventory/product_upload.html",{"form":form})

def product_list(request):
    products=Product.objects.all()
    return render(request,"inventory/product_list.html",{"products": products})
def product_detail(request,id):
    product=Product.objects.get(id=id)
    return render(request,"inventory/product_detail.html",{"product":product})




