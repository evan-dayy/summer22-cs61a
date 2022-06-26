print("hello world")
x = 3.0
y = "john"
print(type(x))
print(type(y))
x = str(x)
print(x)
print(type(x))

x = "Python"
y = "is"
z = "awesome"
print(x, y, z, sep = " ")
print(x + y + z)

print(int(5.6))
range(6)
print(range(6))

for i in range(6):
    print(i)
def func1():
    global x
    x = "today is a good day"
    y = "fuck off"
    print(x,y,sep = "|")
func1()
print(x)
print("%d" % 2.65)
import math
math.ceil(2.3)
math.floor(2.3)

a = 1.35
print("a_1 = %.1f" % a)

import random

print(random.randrange(1, 10))

a = "Hello, World!"
print(a[1])

b = """ today is jun 26,
and it is my first week in Cali,
I am really excited to stay in here"""
print(b)

if "Cali" not in b:
    print("there is not 'Cali' here")
else: print("There is a 'Cali'")

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])
print(b[::-1])
print(b[0::])

print(b.strip())

"""x = input()
print(x.split(","))"""

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

txt = "We are the so-called \"Vikings\" from the north."
print(txt)

a = 1.452
print("a_1 = %0.1f" % a)
print("a_1 = %d" % a)

x = 5
x = complex(x)
print(x)

b = bool(["apple", "cherry", "banana"])
print(b)

print("""
---
---
---
""")

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

x = 200
print(isinstance(x, int))

thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)







thislist = ["apple", "banana", "cherry"]
del thislist

thislist = ["apple", "banana", "cherry"]
[x for x in thislist]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]



newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
# newlist = [x for x in fruits if x != "banana" else "orange" ] wrong way

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
"""
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
"""

points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

x = points.count(9)
print(x)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)

print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)

print(z)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
x = thisdict.get("model")

x = thisdict.items()

print(x) #before the change

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)
  
  
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)


a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i, "\t")


class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(mysillyobject):
    print("Hello my name is " + mysillyobject.name)

p1 = Person("John", 36)
p1.myfunc()

# ------
# ------
# ------
# ------

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname) # Person.__init__(self, fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)



    
    
    