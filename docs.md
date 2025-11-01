# Project Documentation

### 1. Storage

The storage functionality is responsible for data persistence. It is designed in an object-oriented way to handle different types of data.

- **`storage.base_storage.BaseStorage`**: This class provides the basic storage methods, including reading from and writing to JSON files.

- **`storage.products_storage.ProductsStorage`**, **`storage.addons_storage.AddonsStorage`**, **`storage.order_storage.OrderStorage`**: These classes inherit from `BaseStorage` and implement specific CRUD (Create, Read, Update, Delete) methods for products, addons, and orders, respectively. They handle the logic of converting data between dictionary objects and the data models.

- **`storage.storage.STORAGE`**: This global object contains instances of all the specific storage classes, providing a single point of access to all application data.

### 2. Data Models

The `models` package defines the data structure of the application.

- **`models.products.Product`**: Represents a bloom product with properties like item code, name, category, price, and availability.

- **`models.addon.Addon`**: Represents an add-on item with properties like item code, name, price, and availability.

- **`models.order.Order`**: Represents a customer order, which includes an `OrderDetails` object and an `OrderStatus`.

- **`models.order.OrderDetails`**: Contains detailed information about an order, such as the product, addon, customer and recipient names, message, and delivery information.

### 3. User Interface (Menus & Input)

This functionality is responsible for the user interaction with the application through the command-line interface.

- **`menus` package**: This package contains modules for displaying different menus to the user.
    - **`menus.menu_main`**: The main menu of the application.
    - **`menus.menu_inventory`**: The inventory management menu.
    - **`menus.menu_sales`**: The sales management menu.

- **`services.input_module`**: This module provides functions for getting various types of input from the user, with validation and error handling.

### Others
- **`services.table`**: This module provides classes for creating and displaying formatted tables in the console.
- **`utils`**: This module contains utility functions, such as clearing the console and generating random IDs.
