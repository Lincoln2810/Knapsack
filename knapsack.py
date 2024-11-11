import string

class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.value = value
        self.weight = weight
    
    def __repr__(self):
        return self.name
        
items = [
    Item("A", 2, 41),
    Item("B", 3, 42),
    Item("C", 4, 43),
    Item("D", 5, 44),
    Item("E", 6, 45),
]

def getWeight(knapsack):
    weight = 0
    for item in knapsack:
        weight += item.weight
    return weight

def getValue(knapsack):
    total_value = sum(item.value for item in knapsack)
    return total_value

knapsack = [] #object
bestValue = 0 #scalar

def fillKnapsack(index: int):
    global bestValue #you have to call a scalar in the function as a global in python!
    #we are currently deciding, wheter whe should take item[index] or not.
    #exit criteria (when should the recrusion stop?)

    if index == len(items):  # if the end of the items is arrived
        #finding the best way:
#        if (getWeight(knapsack) <= 10):
#          currentValue = getValue(knapsack)
#          if currentValue > bestValue:
#              bestValue = currentValue
#             print(knapsack, currentValue,"$") 
        print(knapsack) # to see the whole operation
        return 
    
    #recrusion code:

    item = items[index] #to find the item in the items list
    
    #turn left (wird zuerst komplett gefüllt, erst dann gehts über zum turn right)
    knapsack.append(item) #add an item into the knapsack
    fillKnapsack(index+1)

    #turn right
    knapsack.remove(item)
    fillKnapsack(index+1)

# filling the knapsack, also the first call of the function "def fillKnapsack"
fillKnapsack(0)