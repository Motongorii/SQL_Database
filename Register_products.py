from main import Product


try:

    product_price = input("Enter product price\n")
    product_quantity = input("Enter product quantity\n")
    product_description = input("Enter product description\n")
    product_color = input("Enter product color\n")

    Product.create(Prod_price=product_price, Prod_quantity=product_quantity,  Prod_description=product_description,  Prod_color=product_color)
    print("Product created successfully")
except:
    print("Failed to create product")


