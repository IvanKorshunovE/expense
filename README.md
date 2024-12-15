# 🚀 ExpenseTracker

A simple Django-based application to manage and track personal and business expenses.
The app follows **Clean Architecture** principles. While this approach may seem like an overkill for a small project, 
as the application scales, the benefits of a layered architecture and dependency injection become more significant.

## 📜 Requirements

- Python 3.x  
- Django  
- Django REST framework  

## ⚙️ Steps to Set Up the Project

1. Clone the repository:
    ```bash
    git clone https://github.com/IvanKorshunovE/expense
    ```

2. Navigate to the project directory:
    ```bash
    cd expense
    ```

3. Set up environment variables:
    ```bash
    nano .env
    ```
    - Configure your `.env` file based on the `env-example` template.

4. Build and start the application using Docker Compose:
    ```bash
    docker-compose -f ./docker/docker-compose.yml up --build -d
    ```

5. Load fixtures (text data) into the database:
    ```bash
    docker-compose -f ./docker/docker-compose.yml exec expense_app sh ./fixtures/load_fixtures.sh
    ```

---

## 📡 Available API Endpoints

### 1. **Expense CRUD Operations**  
**Base URL:** `/expenses/`

- **GET `/expenses/`**  
  Retrieve a list of all expenses.

- **POST `/expenses/`**  
  Create a new expense entry.

- **GET `/expenses/{id}/`**  
  Retrieve details of a specific expense by its ID.

- **PUT `/expenses/{id}/`**  
  Update a specific expense entry by its ID.

- **DELETE `/expenses/{id}/`**  
  Delete a specific expense entry by its ID.

---

### 2. **Filter Expenses**  
Expenses can be filtered using the following query parameters:

- **`date`**: Filter by the specific date of the expense (YYYY-MM-DD).

**Example:**  
Retrieve expenses on **December 1, 2024**:

```http
GET /expenses/?min_date=2024-11-01&max_date=2024-12-01
```

### 2. **Expenses Per Category**  
Get aggregated expenses for **user with ID 5 for December 2024**:

```http
GET /expenses/expenses-per-category/?user_id=5&month=12&year=2024
```