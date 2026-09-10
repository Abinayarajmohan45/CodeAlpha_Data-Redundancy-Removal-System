import sqlite3

# Connect to (or create) the cloud-style database
conn = sqlite3.connect("cloud_database.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
""")
conn.commit()


def is_duplicate(email):
    """Check if this email already exists in the database (redundancy check)."""
    cursor.execute("SELECT * FROM customers WHERE email = ?", (email,))
    return cursor.fetchone() is not None


def add_customer(name, email):
    """Validate and add customer only if not a duplicate."""
    email = email.strip().lower()
    name = name.strip()

    if is_duplicate(email):
        print(f"❌ REDUNDANT: '{email}' already exists. Skipping (false positive prevented).")
        return False
    else:
        cursor.execute("INSERT INTO customers (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print(f"✅ UNIQUE: '{email}' added successfully.")
        return True


def show_all_customers():
    cursor.execute("SELECT * FROM customers")
    rows = cursor.fetchall()
    print("\n--- Current Database ---")
    for row in rows:
        print(row)
    print(f"Total records: {len(rows)}\n")


if __name__ == "__main__":
    print("=== Data Redundancy Removal System ===\n")

    # Sample data - some are duplicates on purpose to test the system
    sample_data = [
        ("Arun Kumar", "arun@example.com"),
        ("Priya S", "priya@example.com"),
        ("Arun Kumar", "arun@example.com"),      # duplicate
        ("Priya S", "PRIYA@example.com"),        # duplicate (case-insensitive)
        ("Karthik R", "karthik@example.com"),
    ]

    for name, email in sample_data:
        add_customer(name, email)

    show_all_customers()

    # Interactive part - let user add their own entries
    print("Now add your own entries (type 'stop' as name to finish):\n")
    while True:
        name = input("Enter name: ")
        if name.lower() == "stop":
            break
        email = input("Enter email: ")
        add_customer(name, email)

    show_all_customers()
    conn.close()