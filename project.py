#function for accessing value and putting into an array
#function for adding all values together
#function for adding tip and tax

print("welcome to benjamin's pizzeria! \nthe waitress is a computer... \nso make sure you double check you're spelling...")

import menu
menu = menu.options
list = []

for key, value in menu.items():
    list.append(key)
print("these are our options:", list)

############# repeat function ##########################################

orders = []
def repeat():
    ans = input("anything else?")
    for key, value in menu.items():
        if ans == key:
            orders.append(value)
            repeat()
        else:
            done = True
    return done

############# main program run ##########################################

ans_one = input("are you ready to order?")
if ans_one == "yes":
    ans = input("what would you like to order?")
    for key, value in menu.items():
        if ans == key:
            orders.append(value)

############# main program run ##########################################
done = False
while done == False:
        done = repeat()

tot = 0
for num in orders:
    tot += num

checks = int(input("how many checks do you need?"))

def split(checks):
    divide = 1
    if checks > 1:
        divide = split
    else:
        divide = 1
    return divide

divide = split(checks)

def tip(tot, divide):
    divide = checks
    sum = 0
    sum =+ tot
    sum += round(tot*.2)
    sum = sum/checks
    return sum
sum = tip(tot, divide)

print(orders)
print("your individual total is", sum, "dollars")
