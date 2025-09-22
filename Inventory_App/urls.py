from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('companyregister/',views.companyregister,name='companyregister'),
    path('userregister/',views.userregister,name='userregister'),
    path('login/',views.login,name='login'),
    path('home/',views.home,name='home'),
    path('logout/', views.logout, name='logout'),
    path('addproducts/', views.addproducts, name='addproducts'),
    path('myproducts/', views.myproducts, name='myproducts'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('companies/', views.companies, name='companies'),
    path('products/<int:id>/', views.products, name='products'),
    path('order/<int:id>/', views.order, name='order'),
    path('vieworders/', views.vieworders, name='vieworders'),
    path('acceptorder/<int:id>/', views.acceptorder, name='acceptorder'),
    path('rejectorder/<int:id>/', views.rejectorder, name='rejectorder'),
    path('myorders/', views.myorders, name='myorders'),
    path('dashboard/', views.dashboard, name='dashboard'),



    
]
