# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold
def calculate_revenue(prices, quantities_sold):
    revenues = []
    for index in range(len(prices)):
        revenues.append(prices[index]*quantities_sold[index])
    return revenues
def formatted_output(revenues):
    revenue_per_product = list(zip(products, revenues))
    revenue_per_product = sorted(revenue_per_product)
    for index in range(len(prices)):
        print(revenue_per_product[index][0],"has total revenue of $",revenue_per_product[index][1])
revenues = calculate_revenue(prices, quantities_sold)
revenue_per_product = sorted(list(zip(products,revenues)))
formatted_output(revenues)
# Example of expected output line (do not remove):