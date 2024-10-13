class House:
    def __init__(self, name, num_of_floors):
        self.name = name
        self.num_of_floors = num_of_floors

    def go_to(self, new_floor: int):
        if new_floor <= self.num_of_floors and new_floor > 0:
            i = 1
            while i <= new_floor:
                print(self.name, i, 'этаж')
                i += 1
        elif new_floor < 1:
            print(self.name, ' вниз дом не построен', new_floor)
        else:
            print(self.name, ' такого этажа пока не существует', new_floor)

    def __len__(self):
        return (self.num_of_floors)

    def __str__(self):
        return (self.name)

    def __eq__(self, other):
      return self.num_of_floors == other.num_of_floors
    def __lt__(self, other):
        return self.num_of_floors < other.num_of_floors
    def __le__(self, other):
        return self.num_of_floors <= other.num_of_floors
    def __gt__(self, other):
        return self.num_of_floors > other.num_of_floors
    def __ge__(self, other):
        return self.num_of_floors >= other.num_of_floors
    def __ne__(self, other):
        return self.num_of_floors != other.num_of_floors
    def __add__(self, value):
        self.num_of_floors += value
        return (self)
    def __radd__(self, value):
        self.num_of_floors += value
        return (self)
    def __iadd__(self, value):
        self.num_of_floors += value
        return (self)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
