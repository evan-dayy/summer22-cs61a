class Cars:
    def __init__(self):
        self.my_cars = []
    def add_car(self, car):
        self.my_cars.append(car)
    def __len__(self):
        return(len(self.my_cars))

my = Cars()
my.add_car('Benz')
my.add_car('Mercedenz')
my.add_car('VM')

print(len(my))

if my:
    print("I have at least one car")
else:
    print("I don't have any car")

# -------
# -------

class Person:
    def __init__(self,fname,lname):
        self.first_name = fname
        self.last_name = lname
    def printname(self):
        print(self.first_name, self.last_name, sep = ",")

y = Person("Evan", "Day")
y.printname()

class Sub_Person(Person):
    def __init__(self, fname, lname, year):
        Person.__init__(self, fname, lname) # super().__init__(fname, lname)
        self.gradyear = year
    def welcome(self):
        print("Welcome!", self.first_name, self.last_name, "to the class of", self.gradyear)
z = Sub_Person("Evan", "Day", 2022)
z.welcome()


# -------
# -------
mytuple = ("apple", "banana", "cherry")
tupleit = iter(mytuple)
print(next(tupleit))
print(next(tupleit))
print(next(tupleit))

mystr = "banana"
striter = iter(mystr)
print(next(striter))
print(next(striter))
print(next(striter))
print(next(striter))
print(next(striter))
print(next(striter))


# -------
# -------
# to create a iterator
class iternum:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = iternum()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

# Stop iteration
class iternum:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myiter = iternum()
for i in myiter:
    print(i)


print("----")
print("----")
print("----")


class numiter():
    def __init__(self):
        self.mynum_set = [] 
    def __iter__(self):
        self.a = 1
        return self # why here cannot be self.a
    def __next__(self):
        x = self.a
        self.a += 1
        self.mynum_set.append(x)
        return x

class childnumiter(numiter):
    def __init__(self):
        super().__init__()
   # def __len__():
     #   return len(self.mynum_set)
    
iterator = childnumiter()

for i in iterator:
    if i > 20:
        break
    else:
        print(i)
        
print(iterator.mynum_set)
print(len(iterator.mynum_set))

iterator2 = numiter()
print(iterator2.mynum_set)
print(len(iterator2.mynum_set))

print("----")
print("----")
print("----")


quantity = 3
sitemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

    
