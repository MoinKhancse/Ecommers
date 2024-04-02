from django.shortcuts import render,redirect,HttpResponse
from adminpanel.models import product,category,product_img
from django.db.models import Q
from django.contrib.auth.hashers import check_password,make_password
from website.models import user_register,wishlist


def wish_counter(request):
    if request.session.has_key('customar_login'):
        wish_list_count = wishlist.objects.filter(customer_id_id = request.session['customar_login']).count()
        return wish_list_count
    else:
        wish_list_count = 0
        return wish_list_count

def home(request):
    cat_name = category.objects.all()
    a = wish_counter(request)
    context = {
        'cat_name': cat_name,
        'wish_list_count': a
    }
    return render(request, 'website/home.html',context)


def show_product_by_cat(request,id):
    cat_name = category.objects.all()
    product_by_cat =product.objects.filter(product_category_id=id).prefetch_related('prod')
    a = wish_counter(request)
    context = {
        'cat_name': cat_name,
        'product_by_cat': product_by_cat,
        'wish_list_count': a
    }
    return render(request, 'website/product_by_cat.html',context)



def shop_detail(request,id):
    cat_name = category.objects.all()
    product_detail =product.objects.filter(id=id).prefetch_related('prod')
    a = wish_counter(request)
    context = {
        'cat_name': cat_name,
        'product_detail': product_detail,
        'wish_list_count': a
    }
    return render(request, 'website/shop_detail.html',context)



def customar_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        password_1 = request.POST.get('password')
        password_2 = request.POST.get('password2')

        if password_1 == password_2:
            customar_reg = user_register(
                username = username,
                email = email,
                mobile = mobile,
                password = make_password(password_1)
            )
            customar_reg.save()
            return redirect('customar_login')   

def customar_login(request):
    if request.method == "POST":
        x = request.POST.get('username')
        y = request.POST.get('password')

        abcd = user_register.customar_chack(x)

        if abcd:
            psw = check_password(y,abcd.password)
            if psw:
                request.session['customar_login'] = abcd.id
                return redirect('home')
            else:
                return redirect('customar_login')
       
        else:
            return redirect('customar_login')
    return redirect('home') 


def customar_logout(request):
    try:
        del request.session['customar_login']
    except:
        pass
    return redirect('home')

def search(request):
    if request.method =='GET':
        p_search = request.GET.get('p_search')
        if p_search != None:
            product_search = product.objects.filter(Q(peoduct_name__icontains = p_search)) 
        else:
            HttpResponse("Product Not Found")

    context = {
        'product_search': product_search
    }
    return render(request, 'website/search.html', context)

def product_shop(request):
    cat_name = category.objects.all()
    product_all = product.objects.all()
    a = wish_counter(request)
    context = {
        'cat_name': cat_name,
        'product_all':product_all,
        'wish_list_count': a
    }
    return render(request, 'website/product_shop.html',context)

def add_to_wish(request,id):
    if request.session.has_key('customar_login'):
        wish_list = wishlist ( 
            product_id_id = id,
            customer_id_id = request.session.get('customar_login', id)
            )
        wish_list.save()
        return redirect('product_shop')
    else:
        return redirect('customar_login')

def wish_details(request):
    if request.session.has_key('customar_login'):
        wish_list = wishlist.objects.filter(customer_id_id = request.session['customar_login'])
        return render(request,'website/wish.html',{'wish_list':wish_list})
    else:
        return redirect('customar_login')

def wish_remove(request,id):
    if request.session.has_key('customar_login'):
        wish_list = wishlist.objects.filter(customer_id_id = request.session['customar_login']).filter(id=id)
        wish_list.delete()
        return redirect('wish_details')
    else:
        return redirect('customar_login')
def add_to_cart(request,product_id,quantity=1):
    cart = request.session.get('cart',{})
    quantity = int(request.POST.get(quantity,1))
    cart[product_id] = cart.get(product_id,0) + quantity

    request.session['cart'] = cart

    return redirect('product_shop')

def contact(request):
    return render(request, 'website/contact.html')
