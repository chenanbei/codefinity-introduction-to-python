# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []
for item in products:
    price = float(products[item][0])
    quantity_sold = int(products[item][1])
    total_sales = price* quantity_sold 
    total_sales_list.append(total_sales)
    min_sales = min(total_sales_list)
    max_sales = max(total_sales_list)
    print("Total sales for",item,":$",total_sales)
total_sum = sum(total_sales_list)
print("Total sum of all sales:$",sum(total_sales_list))
print("Minimum sales:$",min_sales)
print("Maximum sales:$",max_sales)
   
