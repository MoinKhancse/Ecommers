from django.shortcuts import render,redirect,HttpResponse
from adminpanel.models import User,product,product_img,category
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
import os

def index(request):
    return render(request, 'adminpanel/index.html')

def admin_login(request):
    return render(request, 'adminpanel/admin_login.html')

def admin_reg(request):
    return render(request, 'adminpanel/admin_reg.html')

def category_store(request):
    if request.method == 'POST' and request.FILES:
        cat_name = request.POST.get('cat_name')
        
        if len(request.FILES) !=0:
            cat_img = request.FILES['cat_img']
        cat_store = category(
            category_name = cat_name,
            category_img = cat_img
        )
        cat_store.save()
        return redirect('cat_show')  
    return render(request, 'adminpanel/category/add_category.html')

def category_show(request):
    category_show = category.objects.all()
    return render(request, 'adminpanel/category/cat_show.html',{'category_show':category_show})

def edit(request,id):
    edite=category.objects.get(id=id)
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if len(edite.category_img) > 0:
                os.remove(edite.category_img.path)
            edite.category_img=request.FILES['cat_img']
        edite.category_name = request.POST.get('cat_name')
        
        edite.save()
        return redirect('cat_show')
        
    context = {
        'edit_all': edite
    }      
    return render(request, 'adminpanel/category/edit.html',context)

def delete_all(request,id):
    delte = category.objects.get(id=id)
    os.remove(delte.category_img.path)
    delte.delete()
    return redirect('cat_show')

def product_store(request):
    product_name=category.objects.all()
    if request.method == 'POST' and request.FILES:
        product_name = request.POST.get('product_name')
        product_old_price = request.POST.get('product_old_price')
        product_new_price = request.POST.get('product_new_price')
        product_category = request.POST.get('product_category')
        product_image=request.FILES.getlist('product_img')

        product_save = product(
            peoduct_name = product_name,
            product_old_price = product_old_price,
            product_new_price = product_new_price,
            product_category_id = product_category,
        )
        product_save.save()
        product_id = product_save.id

        for i in product_image:
            product_image_store = product_img(
                product_image_all = i,
                product_table_id = product_id
            )
            product_image_store.save()
            return redirect('product_show')

    return render(request, 'adminpanel/product/product_store.html',{'product_name': product_name})

def product_show(request):
    product_show = product.objects.prefetch_related('prod')
    return render(request, 'adminpanel/product/product_show.html',{'product_show':product_show})

def product_details(request,id):
    product_show = product.objects.filter(id=id).prefetch_related('prod')
    return render(request, 'adminpanel/product/product_details.html',{'product_show':product_show})


def product_edit(request,id):
    edit=product.objects.prefetch_related('prod').filter(id=id)
    product_cat = category.objects.all()
        
    context = {
        'product_cat': product_cat,
        'edit_all': edit,
    }
       
    return render(request, 'adminpanel/product/product_edit.html',context,)

def product_update(request,id):
    if request.method == 'POST' and request.FILES:
        product_name = request.POST.get('product_name')
        product_old_price = request.POST.get('product_old_price')
        product_new_price = request.POST.get('product_new_price')
        product_category = request.POST.get('product_category')
        product_image = request.FILES.getlist('product_img')

        product_save = product(
            id = id,
            peoduct_name = product_name,
            product_old_price = product_old_price,
            product_new_price = product_new_price,
            product_category_id = product_category,
        )
        product_save.save()  
        product_id = product_save.id

        for i in product_image:
            abcd = product_img(
                product_image_all = i,
                product_table_id = product_id
            )
            abcd.save()
    else:
        product_name = request.POST.get('product_name')
        product_old_price = request.POST.get('product_old_price')
        product_new_price = request.POST.get('product_new_price')
        product_category = request.POST.get('product_category')

        product_save = product(
            id = id,
            peoduct_name = product_name,
            product_old_price = product_old_price,
            product_new_price = product_new_price,
            product_category_id = product_category,
        )
        product_save.save()  

    return redirect('product_show')
    
def product_delete(request,id):
    delte = product.objects.get(id=id)   
    img = product_img.objects.get(product_table_id = id) 
    os.remove(img.product_image_all.path)
    delte.delete()
    return redirect('product_show')