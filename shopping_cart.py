   
#Create a shopping cart programme that will continuously ask the user for a food profuct and the price of that product.
# Have an exit clause if the user wishes to stop adding more things to their cart.
# At the end show of the food items and the total cost of the items in the cart.

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy or press 'q' to quit: ")
    if food.lower() == 'q':
        break
    else:
        price = float(input(f"Enter the price of the {food}: R"))
        foods.append(food)
        prices.append(price)
        
print("----- YOUR CART -----")

for food in foods:
    print(food, end= " ")
    
for price in prices:
    total += price
    
print("\n")
print(F"Your total is: R{total}") 