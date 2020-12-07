toppings = ["pepperoni","pineapple","cheese","sausage","olives","anchovies","mushrooms"]
prices = [2,6,1,3,2,7,2]
num_pizza = len(toppings)
print("We sell "+str(num_pizza)+" different kinds of pizza!")

pizzas = list(zip(prices, toppings))
pizzas.sort()
print(pizzas)

cheapest_pizza = pizzas[0]
print("Our cheapest pizza is: "+str(cheapest_pizza))

priciest_pizza = pizzas[-1]
print("Our most expensive pizza is: "+str(priciest_pizza))

three_cheapest = pizzas[:3]
print("This is our three cheapest pizza's: "+str(three_cheapest))

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)