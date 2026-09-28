# E-Commerce Web Application

## Project Overview

The **E-Commerce Web Application** is a full-stack online shopping
website developed as part of a Full Stack Web Development internship
project.

The application allows users to browse products, view product details,
search products, add products to a shopping cart, place orders,
create/login to an account, and track orders. An admin panel is also
provided to manage products and update order status.

## Technologies Used

### Frontend

-   HTML5
-   CSS3
-   JavaScript

### Backend

-   Python
-   Django

### Database

-   SQLite / Django Database

### Development Tools

-   Visual Studio Code
-   Django Development Server

## Main Features

### 1. Product Listing

-   Displays available products on the home page.
-   Shows product image, name, price, and Add to Cart button.

### 2. Product Details

-   Users can click a product name to view its detailed information.
-   Displays product description, price, stock, and image.

### 3. Product Search

-   JavaScript-based search functionality.
-   Users can search products by name.

### 4. Shopping Cart

-   Add products to the cart.
-   Increase or decrease product quantity.
-   Remove products from the cart.
-   Automatically calculates product totals and grand total.
-   Cart count is displayed in the navigation bar.

### 5. User Authentication

-   User registration / Sign Up.
-   User Login.
-   User Logout.
-   Displays the logged-in user's username.

### 6. Checkout and Order Placement

-   Collects customer name, email, phone number, and address.
-   Calculates the order total.
-   Saves order information to the database.
-   Displays an order-success confirmation page.

### 7. Order Tracking

-   Users can enter their email address to find their orders.
-   Displays order number, total amount, order date, and current order
    status.

### 8. Admin Panel

-   Django Admin Panel is used to manage products and orders.
-   Admin can view order information.
-   Admin can update order status such as:
    -   Order Placed
    -   Processing
    -   Shipped
    -   Delivered

## Project Workflow

``` text
User visits Home Page
        ↓
Browse / Search Products
        ↓
View Product Details
        ↓
Add Product to Cart
        ↓
Update Cart Quantity
        ↓
Checkout
        ↓
Enter Customer Details
        ↓
Place Order
        ↓
Order Saved in Database
        ↓
Admin Updates Order Status
        ↓
User Tracks Order
```

## Database Models

### Product

The Product model stores: - Product name - Description - Price - Stock -
Product image - Creation date

### Order

The Order model stores: - Customer name - Email - Phone number -
Address - Order status - Total amount - Order creation date

## Project Structure

``` text
e-commerce/
│
├── ecommerce/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── productsapp/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── productsapp/
│
├── db.sqlite3
├── manage.py
└── venv/
```

## How to Run the Project

### 1. Open the project folder

Open the project in Visual Studio Code.

### 2. Activate the virtual environment

On Windows PowerShell:

``` powershell
.env\Scripts\Activate.ps1
```

### 3. Start the Django development server

``` powershell
python manage.py runserver
```

### 4. Open the website

Open:

``` text
http://127.0.0.1:8000/
```

### 5. Open the admin panel

``` text
http://127.0.0.1:8000/admin/
```

## Future Scope

The application can be extended with:

-   Online payment gateway integration
-   Product categories and filters
-   Wishlist functionality
-   Product reviews and ratings
-   Order history for logged-in users
-   Email notifications
-   Improved order tracking with multiple tracking stages
-   Responsive design improvements
-   Deployment to a live hosting platform

## Conclusion

The E-Commerce Web Application demonstrates the development of a
full-stack web application using **HTML, CSS, JavaScript, Python, and
Django**. It implements core e-commerce functionality including product
management, user authentication, shopping cart management, checkout,
order placement, database storage, admin order management, and order
tracking.

This project provides practical experience in connecting a frontend
interface with a Django backend and database to build a functional web
application.
