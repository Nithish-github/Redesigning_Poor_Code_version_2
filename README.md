# Redesigning_Poor_Code
## Library Management System
Overview

The Library Management System is designed to help libraries manage their book collections and user interactions efficiently. It allows for the addition, updating, and deletion of books and users, tracking book availability, and managing checkouts and returns.

Features

    Manage Books: Add, update, delete, list, and search books by title, author, or ISBN.
    Manage Users: Add, update, delete, list, and search users by name or user ID.
    Book Checkout and Return: Handle the checkout and return processes.
    Book Availability: Check the availability of books in real-time.
    Logging: Simple logging of operations for auditing and troubleshooting.

Code Architecture

The Library Management System is structured around the following key components, designed following Object-Oriented Programming principles to ensure modularity and ease of maintenance:

Main Modules

    main.py: The entry point of the application. Handles user interaction through the command-line interface (CLI) and orchestrates the flow of the system.
    book.py: Manages all book-related operations, such as adding, updating, deleting, listing, and searching for books.
    user.py: Manages user-related functionalities, including adding, updating, deleting, listing, and searching for users.
    check.py: Handles the checkout and return processes, keeping track of which books are checked out by which users.

Supporting Modules

    models.py: Defines the data models (Book and User classes) that represent the entities within the system.
    storage.py: Manages data persistence, providing functionalities to save to and load data from a file-based storage system (e.g., JSON or CSV files).

Directory Structure

    LibraryManagementSystem/
    └── main.py
    └── book.py
    └── user.py
    └── check.py
    └── storage.py
    └── models.py
    └── file_storage/
      └── storage.json
    └── logs/
      └── library_management.log
      
Design Decisions

The application is built with Object-Oriented Design principles to ensure modularity, scalability, and maintainability. Each entity, such as books and users, is represented by a class, encapsulating all relevant data and behaviors. The system uses file-based storage (JSON) for persistence, allowing easy data retrieval and updates.

Setup

    Clone the Repository: Clone this repository to your local machine.
    Install Dependencies: Ensure Python 3.x is installed. No external libraries are required for the basic functionality.
    Initialize Storage: On the first run, the system will automatically create necessary storage files in JSON format.

Usage

Run the system from the command line:

    python main.py

Follow the on-screen prompts to interact with the system. You can add books and users, check out and return books, and view available books and user information.
Extending the System

The system is designed to be extensible. To add new features or manage new types of items:

    Add New Classes: For new entities, create new classes following the existing structure.
    Extend Storage: Modify storage.py to handle new data types.
    Update User Interface: Add new options in main.py to interact with the new functionalities.
