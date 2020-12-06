cost_of_premium = 125.00
flat_charge = 20.00

def ground_shippin(weight):
  if weight <= 2:
    cost = weight * 1.50 + flat_charge
  elif weight > 2 and weight <= 6:
    cost = weight * 3.00 + flat_charge
  elif weight > 6 and weight <= 10:
    cost = weight * 4.00 + flat_charge
  else:
    cost = weight * 4.75 + flat_charge
  return cost

def drone_shippin(weight):
  if weight <= 2:
    cost = weight * 4.50
  elif weight > 2 and weight <= 6:
    cost = weight * 9.00
  elif weight > 6 and weight <= 10:
    cost = weight * 12.00
  else:
    cost = weight * 14.25
  return cost

def cheapest_method(weight):
  if ground_shippin(weight) < drone_shippin(weight) and ground_shippin(weight) < cost_of_premium:
    print("Ground shipping is the cheapest!")
  elif drone_shippin(weight) < ground_shippin(weight) and drone_shippin(weight) < cost_of_premium:
    print("Drone shipping is the cheapest!")
  else:
    print("Some how, premuim shipping is the cheapest! Be prepared to pay $" + str(cost_of_premium) + "!")
print(cheapest_method(4.8))
print(cheapest_method(41.5))


# tried adding these statments into print, didn't work. will work on later.
# The cheapest way to ship 4.8 pound package is using ground shipping and it will cost $34.40.
# The cheapest way to ship a 41.5 pound package is using premium ground shipping and it will cost $125.00.

# tried using format to move decimal point to the right to show '.00'. So far, hasn't worked.
# txt = "For only {price:.2f} dollars!"
# print(txt.format(price = 49))