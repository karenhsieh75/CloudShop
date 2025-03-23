# CloudShop CLI

CloudShop CLI is a command-line application built with Python and SQLite, allowing users to manage product categories, product information, and query popular items within categories.

## **Project Structure**

```
cloudshop/
├── cli/                # CLI Interaction Layer (Presentation Layer)
│   ├── main.py         # Main CLI entry point
│   ├── commands.py     # Handles CLI commands
│
├── core/               # Business Logic Layer (Service Layer)
│   ├── user_service.py       # Handles user-related logic
│   ├── listing_service.py    # Handles product-related logic
│   ├── category_service.py   # Handles category-related logic
│
├── data/               # Data Access Layer (Persistence Layer)
│   ├── db.py           # SQLite database operations
│
├── .gitignore          # Git ignore file
├── run.sh              # Script to run the CLI
├── build.sh            # Script to build the project
├── Makefile            # Makefile for build & packaging
└── README.md           # This document
```

### **Layered Architecture Explanation**
1. **Presentation Layer (`cli/`)**
   - Handles user interactions and command parsing.
   - Delegates business logic to the service layer.
   - Ensures the CLI remains responsive and easy to use.

2. **Service Layer (`core/`)**
   - Encapsulates the application's core functionalities.
   - Implements logic for user registration, listing creation, and category management.
   - Acts as an intermediary between the CLI and database layer.

3. **Persistence Layer (`data/`)**
   - Manages SQLite database operations.
   - Ensures efficient data storage and retrieval.
   - Provides reusable database functions to the service layer.

## **Installation & Usage**

### **1. Environment & Dependencies**
- **Programming Language:** Python 3.x (Recommended: Python 3.8+)
- **Database:** SQLite (built into Python standard library)
- **Required Dependencies:** None (only Python standard libraries are used)

Ensure Python is installed before running the application.

```sh
python3 --version
```

### **2. Run CloudShop CLI**
#### **Option 1: Using Shell Scripts**
```sh
chmod +x build.sh run.sh  # Make the scripts executable
./build.sh                # Build the project
./run.sh                  # Start the CLI
```

To reset the database before running:
```sh
./run.sh --reset
```

#### **Option 2: Using Makefile**
```sh
make build  # Build the project
make run    # Start the CLI
```

### **3. CLI Commands**
| Command | Description |
|---------|------------|
| `REGISTER <username>` | Register a new user |
| `CREATE_LISTING <username> '<title>' '<description>' <price> '<category>'` | Create a new listing |
| `DELETE_LISTING <username> <listing_id>` | Delete a listing |
| `GET_LISTING <username> <listing_id>` | Retrieve listing details |
| `GET_CATEGORY <username> '<category>'` | Get all listings in a category |
| `GET_TOP_CATEGORY` <username> | Retrieve the category with the most listings. If multiple categories have the same count, they are sorted lexicographically. |
| `EXIT` | Exit the CLI |

**Example Usage:**
```sh
# Register a user
REGISTER user1

# Create a listing
CREATE_LISTING user1 'Phone model 8' 'Black color, brand new' 1000 'Electronics'

# Retrieve a listing
GET_LISTING user1 100001

# Retrieve a category
GET_CATEGORY user1 'Electronics'

# Retrieve the most listed category
GET_TOP_CATEGORY
```

## **Technical Details**

### **1. Programming Environment**
- **Python Version:** Python 3.8+
- **Database:** SQLite (via Python’s built-in `sqlite3` module)
- **Dependencies:** No external libraries required

### **2. `GET_TOP_CATEGORY` Query Optimization**
The `GET_TOP_CATEGORY` command retrieves the category with the most listings, sorting lexicographically if there is a tie, using the following optimized SQL query:
```sql
SELECT category
FROM listings
GROUP BY category
HAVING COUNT(*) = (
    SELECT MAX(category_count)
    FROM (
        SELECT COUNT(*) AS category_count
        FROM listings
        GROUP BY category
    )
)
ORDER BY category ASC;
```

This query uses `GROUP BY` to count listings per category and ensures that if multiple categories have the same highest count, they are returned in lexicographical order.

### **3. Using an Index for Performance Optimization**
To further improve performance when querying the top category, an **index is created on `listings.category`**. This helps speed up `COUNT(*)` operations, especially when dealing with large datasets.
```sql
CREATE INDEX IF NOT EXISTS idx_category ON listings(category);
```

This index allows SQLite to efficiently count and group listings by category without scanning the entire table sequentially, significantly reducing query execution time.
