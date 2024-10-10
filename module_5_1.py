class House:
    def __init__(self, name, num_of_floors):
        self.name = name
        self.num_of_floors = num_of_floors

    def go_to (self, new_floor : int):
        if new_floor <= self.num_of_floors:
            i=1
            while i <= new_floor:
                print (i)
                i += 1
        else: print('Такого этажа не существует')


h1 = House ('ЖК Горский', 18)
h2 = House ('Домик в деревне', 2)

h1.go_to(5)
h2.go_to (2)
