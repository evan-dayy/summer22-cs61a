def greeting1(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

class numiter():
    def __iter__(self):
        self.a = 1
        return self # why here cannot be self.a
    def __next__(self):
        x = self.a
        self.a += 1
        return x