# Inventory Management System

This is a Django-based Inventory Management System for managing companies, products, and orders. The project includes user authentication, company profiles, product management, and order tracking.

## Features
- Company registration and profile management
- Product CRUD operations
- Order management
- User authentication (login/register)
- Dashboard and reporting




## Screenshots

Below are actual screenshots from the application, located in the `Screens/` folder. Each image is displayed at a readable size for clarity.

<div align="center">
   <img src="Screens/image_1.png" alt="Login Page" width="600" />
   <br><b>Login Page</b>
   <br><br>
   <img src="Screens/image_2.png" alt="Dashboard" width="600" />
   <br><b>Dashboard</b>
   <br><br>
   <img src="Screens/image_3.png" alt="Product List" width="600" />
   <br><b>Product List</b>
   <br><br>
   <img src="Screens/image_7.png" alt="Add Product" width="600" />
   <br><b>Add Product</b>
   <br><br>
   <img src="Screens/image_8.png" alt="Edit Product" width="600" />
   <br><b>Edit Product</b>
   <br><br>
   <img src="Screens/image_9.png" alt="Orders List" width="600" />
   <br><b>Orders List</b>
   <br><br>
   <img src="Screens/image_12.png" alt="Order Details" width="600" />
   <br><b>Order Details</b>
   <br><br>
   <img src="Screens/image_13.png" alt="Company Profile" width="600" />
   <br><b>Company Profile</b>
   <br><br>
   <img src="Screens/image_15.png" alt="User Registration" width="600" />
   <br><b>User Registration</b>
   <br><br>
   <img src="Screens/image_16.png" alt="User List" width="600" />
   <br><b>User List</b>
   <br><br>
   <img src="Screens/image_18.png" alt="Reports" width="600" />
   <br><b>Reports</b>
   <br><br>
   <img src="Screens/image_19.png" alt="Settings" width="600" />
   <br><b>Settings</b>
   <br><br>
   <img src="Screens/image_22.png" alt="Notifications" width="600" />
   <br><b>Notifications</b>
   <br><br>
   <img src="Screens/image_23.png" alt="Help / About" width="600" />
   <br><b>Help / About</b>
   <br><br>
   <img src="Screens/image_25.png" alt="Miscellaneous 1" width="600" />
   <br><b>Miscellaneous 1</b>
   <br><br>
   <img src="Screens/image_26.png" alt="Miscellaneous 2" width="600" />
   <br><b>Miscellaneous 2</b>
</div>

> Screenshots are for demonstration. Update descriptions as needed to match your actual screen content.

## Project Structure
- `Inventory_App/`: Main Django app containing models, views, and migrations
- `Inventory_Management_System/`: Django project settings and configuration
- `static/`: Static files (CSS, JS, images)
- `templates/`: HTML templates for the web interface
- `db.sqlite3`: SQLite database file
- `manage.py`: Django management script

## Setup Instructions
1. **Clone the repository**
2. **Install dependencies**:
   - Ensure you have Python 3.8+
   - Install Django: `pip install django`
3. **Apply migrations**:
   - `python manage.py migrate`
4. **Create a superuser**:
   - `python manage.py createsuperuser`
5. **Run the development server**:
   - `python manage.py runserver`
6. **Access the app**:
   - Open `http://127.0.0.1:8000/` in your browser

## License
This project is for educational purposes.
