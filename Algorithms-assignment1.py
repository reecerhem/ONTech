 #Name: Sherice Morris
 #ID: 100850092
 #Course: Algorithms & Data Structuring
 


import time

# Data structure to represent a product
class Product:
    def __init__(self, id, name, price, category):
        self.id = id
        self.name = name
        self.price = price
        self.category = category

# Function to load product data from a file into a list of Product objects
def load_data(product_data):
    products = []
    with open(product_data, 'r') as file:
        for line in file:
            id, name, price, category = line.strip().split(',')
            products.append(Product(int(id), name, float(price), category))
    return products

# Function to insert a new product into the list of products
def insert_product(products, new_product):
    products.append(new_product)

# Function to update an existing product
def update_product(products, product_id, new_price):
    for product in products:
        if product.id == product_id:
            product.price = new_price
            break

# Function to delete a product
def delete_product(products, product_id):
    products[:] = [product for product in products if product.id != product_id]

# Function to search for a product by ID
def search_product(products, product_id):
    for product in products:
        if product.id == product_id:
            return product
    return None

# Insertion Sort algorithm for sorting products by price
def insertion_sort(products):
    for i in range(1, len(products)):
        key = products[i]
        j = i - 1
        while j >= 0 and products[j].price > key.price:
            products[j + 1] = products[j]
            j -= 1
        products[j + 1] = key

# Function to print product details
def print_product(product):
    if product:
        print(f"ID: {product.id}, Name: {product.name}, Price: {product.price}, Category: {product.category}")
    else:
        print("Product not found.")

# Main function
def main():
    # Load data from file
    products = load_data("C:\\Users\\Sherice\\AppData\\Local\\Programs\\Python\\Python312\\product_data.txt")

    # Interactive menu
    while True:
        print("\n1. Insert a new product")
        print("2. Update an existing product")
        print("3. Delete a product")
        print("4. Search for a product")
        print("5. Sort products by price")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == '1':
            id = int(input("Enter product ID: "))
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            category = input("Enter product category: ")
            new_product = Product(id, name, price, category)
            insert_product(products, new_product)
            print("Product inserted successfully.")

        elif choice == '2':
            product_id = int(input("Enter product ID to update: "))
            new_price = float(input("Enter new price: "))
            update_product(products, product_id, new_price)
            print("Product updated successfully.")

        elif choice == '3':
            product_id = int(input("Enter product ID to delete: "))
            delete_product(products, product_id)
            print("Product deleted successfully.")

        elif choice == '4':
            search_id = int(input("Enter product ID to search: "))
            searched_product = search_product(products, search_id)
            print_product(searched_product)
        #Insertion sort function being sorted by price
        elif choice == '5':
            start_time = time.perf_counter()
            insertion_sort(products)
            end_time = time.perf_counter()
            print("\nSorted Products by Price:")
            for product in products:
                print_product(product)
            sorting_time = end_time - start_time
            print(f"\nSorting Time: {sorting_time:.14f} seconds")
     
            
            # Best case: already sorted data
            sorted_products = load_data("C:\\Users\\Sherice\\AppData\\Local\\Programs\\Python\\Python312\\product_data.txt")
            start_time = time.perf_counter()
            insertion_sort(sorted_products)
            end_time = time.perf_counter()
            print("\nTime taken for sorting already sorted data:", end_time - start_time, "seconds")

            # Worst case: data in reverse order
            reverse_sorted_products = sorted(products, key=lambda x: x.price, reverse=True)
            start_time = time.perf_counter()
            insertion_sort(reverse_sorted_products)
            end_time = time.perf_counter()
            print("Time taken for sorting data in reverse order:", end_time - start_time, "seconds")
            
        elif choice == '6':
            print("Exiting...goodbye")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
