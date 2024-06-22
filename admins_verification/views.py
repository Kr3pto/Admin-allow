from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Product
from django.contrib.admin.views.decorators import staff_member_required


def home(request):
    products = Product.objects.filter(approved=True)
    return render(request, 'home.html', {'products': products})


@login_required
def user_dashboard(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('user_dashboard')
    else:
        form = ProductForm()
    products = Product.objects.filter(user=request.user)
    return render(request, 'user_dashboard.html', {'form': form, 'products': products})


@staff_member_required

@staff_member_required
def approve_products(request):
    products = Product.objects.filter(approved=False)
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        action = request.POST.get('action')
        product = get_object_or_404(Product, id=product_id)
        
        if action == 'approve':
            product.approved = True
            product.save()
        elif action == 'delete':
            product.delete()
        
        return redirect('approve_products')
    return render(request, 'approve_products.html', {'products': products})