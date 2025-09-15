#EXERCICE 1
print("Hello World "*4)


#EXERCICE 2
result = 99**3 *8
print(result)

#EXERCICE 3
user_name = input("enter your name: ")
if user_name == "maryama":
    print("woow!! whe have the same name")
else:
    print("you better get my name right hahaha")

#EXERCICE 4
height = int(input("enter your height in cm to verify if you're able to ride: "))
if height >145:
    print("you're able to ride")
else:
    print ("sorry your height is not enough to ride")

#EXERCICE 5
my_fav_numbers ={1,9,22,11,64}
my_fav_numbers.update([6,4])
my_fav_numbers.remove(64)

friend_fav_numbers = {108,32,90,86}

our_fav_numbers= my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)


#EXERCICE 6
tupLy= (19,98, 0,23)
"""tuple is immutable so w cant add element to it"""

#EXERCICE 7
basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(0,"Apples")
print(basket.count("Apples"))
basket.clear()
print(basket)


#EXERCICE 8
sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]
while "Pastrami sandwich" in sandwich_orders:
    sandwich_orders.remove("Pastrami sandwich")
print(sandwich_orders)

finished_sandwiches= []
while sandwich_orders:
    sandw = sandwich_orders.pop(0)
    finished_sandwiches.append(sandw)
    print("I made your "+ str(sandw))