import mysql.connector

# ---- DB Connection ----
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="123@ussrR",     # write your MySQL password
        database="shopdb"
    )


# ---- CRUD OPERATIONS ----

def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter price: "))

    conn = connect_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO product (name, price) VALUES (%s, %s)", (name, price))
    conn.commit()
    conn.close()

    print("\nProduct added successfully!\n")


def view_products():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM product")
    rows = cur.fetchall()
    conn.close()

    print("\n---- PRODUCT LIST ----")
    for r in rows:
        print(f"ID: {r[0]} | Name: {r[1]} | Price: {r[2]}")
    print()


def update_product():
    pid = input("Enter Product ID to update: ")

    name = input("New name: ")
    price = float(input("New price: "))

    conn = connect_db()
    cur = conn.cursor()
    cur.execute("UPDATE product SET name=%s, price=%s WHERE id=%s", (name, price, pid))
    conn.commit()
    conn.close()

    print("\nProduct updated!\n")


def delete_product():
    pid = input("Enter Product ID to delete: ")

    conn = connect_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM product WHERE id=%s", (pid,))
    conn.commit()
    conn.close()

    print("\nProduct deleted!\n")


# ---- MAIN MENU ----

while True:
    print("====== PRODUCT CRUD MENU ======")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    if choice == "1":
        add_product()
    elif choice == "2":
        view_products()
    elif choice == "3":
        update_product()
    elif choice == "4":
        delete_product()
    elif choice == "5":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice!\n")
