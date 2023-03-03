from main import Product

products = Product.select()
for product in products:
    print(product.Prod_price, product.Prod_quantity, product.Prod_description, product.Prod_color)