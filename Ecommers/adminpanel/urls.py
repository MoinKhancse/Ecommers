from django.urls import path
from adminpanel import views

urlpatterns = [
    path('index',views.index, name='index'),
    path('admin_login',views.admin_login, name='admin_login'),
    path('admin_reg',views.admin_reg, name='admin_reg'),

    #===========================================================#

    path('add_category',views.category_store, name='add_category'),
    path('cat_show',views.category_show, name='cat_show'),
    path('edit/<int:id>/', views.edit ,name='edit'),
    path('delete/<int:id>/',views.delete_all, name='delete'),

    #========================================================
    path('product_store',views.product_store, name='product_store'),
    path('product_show',views.product_show, name='product_show'),
    path('product_details/<int:id>/',views.product_details, name="product_details"),

    path('product_edit/<int:id>/',views.product_edit, name='product_edit'),
    path('product_update/<int:id>/',views.product_update, name='product_update'),
    path('product_delete/<int:id>/',views.product_delete, name='product_delete'),
]