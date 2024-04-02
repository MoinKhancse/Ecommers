from django.urls import path
from website import views

urlpatterns = [
    path('',views.home, name='home'),
    
    path('product_by_cat/<int:id>/',views.show_product_by_cat, name='product_by_cat'),

    path('shop_detail/<int:id>/',views.shop_detail, name='shop_detail'),

    path('customar_rag',views.customar_signup, name='customar_rag'),

    path('customar_login',views.customar_login, name='customar_login'),

    path('customar_logout',views.customar_logout, name='customar_logout'),

    path('search',views.search,name='search'),

    path('product_shop',views.product_shop, name='product_shop'),

    path('contact',views.contact ,name='contact'),

    path('wish_list/<int:id>/',views.add_to_wish, name='wish_list'),

    path('wish_details',views.wish_details, name='wish_details'),

    path('wish_remove/<int:id>/',views.wish_remove,name='wish_remove'),

    path('add_to_cart/<int:product_id>/',views.add_to_cart,name='add_to_cart')

]