# Inventory Management System

This is a Django-based Inventory Management System for managing companies, products, and orders. The project includes user authentication, company profiles, product management, and order tracking.

## Features
- Company registration and profile management
- Product CRUD operations
- Order management
- User authentication (login/register)
- Dashboard and reporting




## Screenshots

Below are actual screenshots from the application, located in the `Screens/` folder. The images will display correctly on GitHub if you commit the `Screens` folder and all images.

| Screen            | Preview |
|-------------------|---------|
| Login Page        | ![Login Page](Screens/image_1.png) |
| Dashboard         | ![Dashboard](Screens/image_2.png) |
| Product List      | ![Product List](Screens/image_3.png) |
| Add Product       | ![Add Product](Screens/image_7.png) |
| Edit Product      | ![Edit Product](Screens/image_8.png) |
| Orders List       | ![Orders List](Screens/image_9.png) |
| Order Details     | ![Order Details](Screens/image_12.png) |
| Company Profile   | ![Company Profile](Screens/image_13.png) |
| User Registration | ![User Registration](Screens/image_15.png) |
| User List         | ![User List](Screens/image_16.png) |
| Reports           | ![Reports](Screens/image_18.png) |
| Settings          | ![Settings](Screens/image_19.png) |
| Notifications     | ![Notifications](Screens/image_22.png) |
| Help / About      | ![Help / About](Screens/image_23.png) |
| Miscellaneous 1   | ![Miscellaneous 1](Screens/image_25.png) |
| Miscellaneous 2   | ![Miscellaneous 2](Screens/image_26.png) |

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
