produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]
groceries = [produce, dairy]
for grocery in groceries:
    print(grocery)
    for item in grocery:
        print(item)