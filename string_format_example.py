from itertools import count

price = 50
txt = "The Price is {} dollars"
print(txt.format(price))


txt = "The price is {:.8f} dollars"
print(txt.format(price))

txt = "{} with {} Quantity, total is {}."
itemName = "Eggs"
count = 10
total = count*7
print(txt.format(itemName, count, total))

my_order = "I want {1} {0} for {2:.2f} rupees"
print(my_order.format(itemName, count, total))

my_order = "I want {count} {itemName} for {total:.2f} rupees"
print(my_order.format(itemName='Ice Cream', count=1, total=150))
