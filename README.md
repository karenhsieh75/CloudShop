# CloudShop CLI

CloudShop CLI is a command-line application built with Python and SQLite, allowing users to manage product categories, product information, and query popular items within categories.

## **Project Structure**

This project follows a **medium-sized architecture**, organized by business logic layers:
```
cloudshop/
├── cli/                # CLI Interaction Layer (Presentation Layer)
│   ├── main.py         # Main CLI entry point
│   ├── commands.py     # Handles CLI commands
│
├── core/               # Business Logic Layer (Service Layer)
│   ├── user_service.py       # Handles user-related logic
│   ├── listing_service.py    # Handles product-related logic
│   ├── category_service.py   # Handles category management logic
│
├── data/               # Data Access Layer (Persistence Layer)
│   ├── db.py           # SQLite database operations
│
├── tests/              # Testing
│   ├── test_users.py
│   ├── test_listings.py
│   ├── test_categories.py
│
├── .gitignore          # Git ignore file
├── run.sh              # Script to run the CLI
├── build.sh            # Script to build the project
├── requirements.txt    # Dependency management
├── Makefile            # Makefile for build & packaging
└── README.md           # This document
```

---

## **Installation & Usage**

### **1. Environment & Dependencies**
- **Programming Language:** Python 3.x (Recommended: Python 3.8+)
- **Database:** SQLite (built into Python standard library)
- **Required Dependencies:** None (only Python standard libraries are used)

Ensure Python is installed before running the application.

```sh
python3 --version
```

If Python is not installed, download it from [Python's official site](https://www.python.org/downloads/).

### **2. Run CloudShop CLI**
```sh
chmod +x run.sh  # Make the script executable
./run.sh         # Start the CLI
```

To reset the database before running:
```sh
./run.sh --reset
```

### **3. CLI Commands**
| Command | Description |
|---------|------------|
| `REGISTER <username>` | Register a new user |
| `CREATE_LISTING <username> '<title>' '<description>' <price> '<category>'` | Create a new listing |
| `DELETE_LISTING <username> <listing_id>` | Delete a listing |
| `GET_LISTING <username> <listing_id>` | Retrieve listing details |
| `GET_CATEGORY <username> '<category>'` | Get all listings in a category |
| `GET_TOP_CATEGORY` | Retrieve the category with the most listings. If multiple categories have the same count, they are sorted lexicographically. |
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

---

## **Technical Details**

### **1. Programming Environment**
- **Python Version:** Python 3.8+
- **Database:** SQLite (via Python’s built-in `sqlite3` module)
- **Dependencies:** No external libraries required

### **2. `get_top_category` Query Optimization**
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

---

## **Development Guidelines**
- `__pycache__/` and `*.db` should be added to `.gitignore` to avoid committing unnecessary files.
- CLI command parsing and business logic are separated for better maintainability.
- Additional features like `UPDATE_LISTING` or `FILTER_BY_PRICE` could be implemented in future extensions.

For any issues or suggestions, feel free to contact the developers or submit an issue!
