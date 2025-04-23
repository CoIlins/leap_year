class SimpleClass:
    ...

class Person:
    pass

class Animal:
  ...

class Classy:
    varia = 2
def method(self):
    print(self.varia)


object_one= Classy()
object_two=Classy()

object_one.varia = 3

object_two.varia = 5
print(object_one.varia)
print(object_two.varia)

class Transport:
    def __init__(self, air, water):
       self.air = air
       self.water = water


obj_transport = Transport("Beluga", "Hovercraft")
obj2 = Transport( "Jet", "Boat")


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

x  = Person("John", "Doe")
x.printname()


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item_name, qty):
        item = (item_name, qty)
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break
                #This method computes the number of items in the cart

    def calculate_total(self):
        total = 0
        for item in self.items:
            total +=item[1]
        return total

cart = ShoppingCart()


#add items to our cart
cart.add_item("Kiwi", 100)
cart.add_item("Papaya", 10)
cart.add_item("Orange", 90)

print("Current Items In Cart")

for item in cart.items:
    print(item[0], " ", item[1] )

total_qty = cart.calculate_total()
print("Total Quantity: ", total_qty)

# print(obj_transport.air, obj_transport.water)
# print(obj2.air, obj2.water)
