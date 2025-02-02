# PYTHON PROGRAMMING LANGUAGE, EACH DATA TYPE IS AN OBJECT
# THAT HAS BEEN INSTANTIATED EARLIER BY A CLASS

# CREATION OF CLASS
class Item:
    # MAGIC METHODS, ARE METHODS WITH DOUBLE UNDERSCORE
    # PROBLEM WE EXPERIENCE IS WE HARDCODE CODING VARIABLES
    
    
    # THIS IS HOW WE USE THE __init__ METHOD
    # TAKE NOTES:
    # 1. IN MANDATORY AND NON-MANDATORY PARAMETERS, WHEN YOU CURRENTLY HAVE NO IDEA FOR A SPECIFIC ITEM
    # FOR EXAMPLE IN QUANTITY, YOU COULD ASSIGN 0 TO IT, LIKE quantity=0
    
    # 2. YOU CAN ASSIGN ATTRIBUTES TO SPECIFIC INSTANCES INDIVIDUALLY
    def __init__(self, name: str, price: float, quantity=0): # ASSIGNING DATA TYPES HERE
       #print(f"An instance created: {name}")
       self.name = name
       self.price = price
       self.quantity = quantity
       
    # EACH METHOD THAT WE ASSIGN IN CLASSES THEN THE OBJECT ITSELF IS PASSED IN ARGUMENT
    def calculate_total_price(self):
        # IN HERE, YOU NEED FIRST TO VALIDATE THE DATA TYPES OF THE VALUES THAT WE ARE PASSING IN
        return self.price * self.quantity

# CREATION WHERE WE WILL INSTANTIATE SOME OBJECTS OF THIS CLASS
item1 = Item("Phone", 100, 5)
# item1.price = 100
# item1.quantity = 5
# print(item1.calculate_total_price(item1.price, item1.quantity))

item2 = Item("Laptop", 1000, 3)
# item2.price = 1000
# item2.quantity = 3
# print(item2.calculate_total_price(item2.price, item2.quantity))

# METHODS MEAN TWO FUNCTIONS THAT ARE INSIDE THE CLASSES
# IF YOU MAKE FUNCTIONS INSIDE CLASSES IT IS CALLED METHODS

# item2.has_numpad = False
print(item1.calculate_total_price())
print(item2.calculate_total_price())
