from django.shortcuts import render, redirect
from django.contrib import messages
from . models import *
from django.core.paginator import Paginator
from decimal import Decimal

# Create your views here.

def index(request):
    companies = Company.objects.all()

    return render(request, 'index.html',{'companies':companies})

def about(request):
    return render(request, 'about.html')

def companyregister(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')
        image = request.FILES['image']
       

        if password != confirm:
            messages.error(request, "Passwords do not match!")
            return redirect('register')  # replace with your actual URL name

        

        # Check if user already exists
        if Company.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('userregister')

        Company.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            address=address,
            password=password,
            profile=image

        ).save()
        messages.success(request, "Registration successful!")
        return redirect('login')  # replace with your login page

    return render(request, 'companyregister.html')

def userregister(request):
    if request.method == 'POST':
        full_name = request.POST.get('fullname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm')

        if password != confirm:
            messages.error(request, "Passwords do not match!")
            return redirect('userregister')  # replace with your actual URL name

        

        # Check if user already exists
        if UserModel.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered.")
            return redirect('userregister')

        UserModel.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            address=address,
            password=password
        ).save()
        messages.success(request, "Registration successful!")
        return redirect('login')  # replace with your login page

    return render(request, 'usersregister.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if Company.objects.filter(email=email, password=password).exists():
            request.session['email'] = email
            request.session['login'] = 'Company'
            return redirect("home")
        elif UserModel.objects.filter(email=email, password=password).exists():
            request.session['email'] = email
            request.session['login'] = 'User'
            return redirect("home")
        else:
            messages.error(request, "Invalid Email or Password")
            return redirect('login')

    return render(request, 'login.html')


def home(request):
    login = request.session['login']
    companies = Company.objects.all()
    return render(request, 'home.html', {'login':login,'companies':companies})

def logout(request):
    del request.session['login']
    del request.session['email']
    return redirect('index')

def addproducts(request):
    login = request.session['login']
    email = request.session['email']
    if request.method == "POST":
        product_name = request.POST.get("product_name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        company = Company.objects.get(email=email)
        product = Products.objects.create(
            name=product_name,
            price=price,
            description=description,
            quantity=quantity,
            company=company,
            total_qty=quantity,
            )
        product.save()
        messages.success(request, 'Product Added Successfully!')
        return redirect('addproducts')
    return render(request, 'addproducts.html', {'login':login})

def myproducts(request):
    login = request.session['login']
    email = request.session['email']
    company = Company.objects.get(email=email)
    products = Products.objects.filter(company=company)
    paginator = Paginator(products, 4)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)  
    return render(request, 'myproducts.html', {'data':page_obj, 'login':login})

def delete(request, id):
    product = Products.objects.get(id=id)
    product.delete()
    messages.success(request, 'Product Deleted Successfully!')
    return redirect('myproducts')

def update(request, id):
    login = request.session['login']
    product = Products.objects.filter(id=id)
    if request.method == "POST":
        product = Products.objects.get(id=id)

        product.name = request.POST.get("product_name")
        product.price = request.POST.get("price")
        product.description = request.POST.get("description")
        product.quantity += int(request.POST.get("quantity"))
        # if product.quantity > request.POST.get("quantity"):
        product.total_qty = product.total_qty + int(request.POST.get("quantity"))
        product.save()
        messages.success(request, 'Product Updated Successfully!')
        return redirect('myproducts')
    return render(request, 'updateproduct.html', {'product':product, 'id':id, 'login':login})


def companies(request):
    login = request.session['login']
    companies = Company.objects.all()
    return render(request, 'companies.html', {'companies':companies, 'login':login})

def products(request, id):
    login = request.session['login']
    company = Company.objects.get(id=id)
    products = Products.objects.filter(company=company)
    paginator = Paginator(products, 4)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)  
    return render(request, 'products.html', {'data':page_obj, 'login':login})
from django.core.mail import send_mail
from django.conf import settings
from decimal import Decimal
from .models import UserModel, Products, Orders

def order(request, id):
    login = request.session['login']
    email = request.session['email']
    user = UserModel.objects.get(email=email)

    products = Products.objects.filter(id=id)
    if request.method == 'POST':

        qty = Decimal(request.POST['quantity'])
        address = request.POST['address']
        total = products[0].price * qty
        order = Orders.objects.create(
            customer=user,
            product=products[0],
            ord_qty=qty,
            total_price=total,
            address=address
        )
        order.save()

        # Sending Email to the Customer (User)
        customer_name = user.full_name
        customer_email = user.email
        product_name = products[0].name
        product_price = products[0].price

        send_mail(
            subject='Order Placed Successfully',
            message=(
                f'Hello {customer_name},\n\n'
                f'Your order has been placed successfully!\n\n'
                f'Order Details:\n'
                f'Product Name: {product_name}\n'
                f'Product Price: ₹{product_price}\n'
                f'Quantity: {qty}\n'
                f'Total Price: ₹{total}\n\n'
                f'Shipping Address: {address}\n\n'
                f'Thank you for shopping with us!'
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[customer_email],
            fail_silently=False,
        )

        # Sending Email to the Company (Owner)
        company_name = products[0].company.full_name  # Assuming `company` is a ForeignKey
        company_email = products[0].company.email

        send_mail(
            subject='New Order Placed',
            message=(
                f'Hello {company_name},\n\n'
                f'A new order has been placed for your product {product_name}.\n\n'
                f'Order Details:\n'
                f'Product Name: {product_name}\n'
                f'Product Price: ₹{product_price}\n'
                f'Quantity: {qty}\n'
                f'Total Price: ₹{total}\n\n'
                f'Customer Details:\n'
                f'Name: {customer_name}\n'
                f'Email: {customer_email}\n'
                f'Shipping Address: {address}\n\n'
                f'Please process the order accordingly.'
            ),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[company_email],
            fail_silently=False,
        )

        messages.success(request, 'Order Placed Successfully!')
        return redirect('myorders')

    return render(request, 'order.html', {'id': id, 'products': products, 'login': login, 'user': user.full_name})


def vieworders(request):
    login = request.session['login']
    email = request.session['email']
    company = Company.objects.get(email=email)
    orders = Orders.objects.filter(product__company=company)
    paginator = Paginator(orders, 4)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)
    return render(request, 'vieworders.html', {'data':page_obj, 'login':login})

from django.core.mail import send_mail
from django.conf import settings
from .models import Orders, Products

def acceptorder(request, id):
    data = Orders.objects.get(id=id)
    product = Products.objects.get(id=data.product.id)
    
    # Reduce product quantity
    product.quantity -= data.ord_qty
    product.save()

    # Update order status to 'Accepted'
    data.status = 'Accepted'
    data.save()

    # Send email to customer (User)
    customer_name = data.customer.full_name
    customer_email = data.customer.email
    product_name = product.name
    total_price = data.total_price

    send_mail(
        subject='Your Order has been Accepted',
        message=(
            f'Hello {customer_name},\n\n'
            f'Your order for {product_name} has been accepted.\n\n'
            f'Order Details:\n'
            f'Product Name: {product_name}\n'
            f'Total Price: ₹{total_price}\n\n'
            f'We are preparing your order. Please wait for further updates.'
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[customer_email],
        fail_silently=False,
    )

    # Send email to company (Owner)
    company_name = product.company.full_name
    company_email = product.company.email

    send_mail(
        subject='Order Accepted',
        message=(
            f'Hello {company_name},\n\n'
            f'Your product {product_name} order has been accepted.\n\n'
            f'Order Details:\n'
            f'Product Name: {product_name}\n'
            f'Quantity: {data.ord_qty}\n'
            f'Total Price: ₹{total_price}\n\n'
            f'Please prepare the product for shipping.'
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[company_email],
        fail_silently=False,
    )

    messages.success(request, 'Order Accepted Successfully!')
    return redirect('vieworders')


def rejectorder(request, id):
    data = Orders.objects.get(id=id)
    product = data.product
    # Send email to customer (User)
    customer_name = data.customer.full_name
    customer_email = data.customer.email
    product_name = product.name

    send_mail(
        subject='Your Order has been Rejected',
        message=(
            f'Hello {customer_name},\n\n'
            f'We regret to inform you that your order for {product_name} has been rejected.\n\n'
            f'For more information, please contact our support team.'
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[customer_email],
        fail_silently=False,
    )

    # Send email to company (Owner)
    company_name = product.company.full_name
    company_email = product.company.email

    send_mail(
        subject='Order Rejected',
        message=(
            f'Hello {company_name},\n\n'
            f'An order for your product {product_name} has been rejected.\n\n'
            f'Please check your dashboard for further details.'
        ),
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[company_email],
        fail_silently=False,
    )

    data.status = 'Rejected'
    data.save()
    messages.success(request, 'Order Rejected Successfully!')
    return redirect('vieworders')


def myorders(request):
    login = request.session['login']
    email = request.session['email']
    user = UserModel.objects.get(email=email)
    orders = Orders.objects.filter(customer=user)
    paginator = Paginator(orders, 4)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)
    return render(request, 'vieworders.html', {'data':page_obj, 'login':login})


from django.shortcuts import render
from .models import Orders, Products
from django.db.models import Sum, Count

def dashboard(request):
    login = request.session['login']
    email = request.session['email']

    # Filter only orders related to the logged-in company
    company_orders = Orders.objects.filter(product__company__email=email)

    # Unique customers
    unique_customers_count = company_orders.values('customer').distinct().count()

    # Total orders
    total_orders = company_orders.count()
    income = Orders.objects.filter(product__company__email=email,status='Accepted')
    # Total income (sum of total_price)
    total_income = income.aggregate(total_income=Sum('total_price'))['total_income'] or 0

    # Total number of products listed by the company
    total_products = Products.objects.filter(company__email=email).count()
    products = Products.objects.filter(company__email=email)

    context = {
        'login': login,
        'unique_customers_count': unique_customers_count,
        'total_orders': total_orders,
        'total_income': total_income,
        'total_products': total_products,
        'products': products
    }

    return render(request, 'dashboard.html', context)
