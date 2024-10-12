class House:
    def __init__(self, name, num_of_floors):
        self.name = name
        self.num_of_floors = num_of_floors

    def go_to (self, new_floor : int):
        if new_floor <= self.num_of_floors and new_floor > 0:
            i=1
            while i <= new_floor:
                print (self.name, i, 'этаж')
                i += 1
        elif new_floor < 1:
            print ( self.name, ' вниз дом не построен', new_floor)
        else: print( self.name, ' такого этажа пока не существует', new_floor)

    def __len__(self):
        return (self.num_of_floors)

    def __str__(self):
        return (self.name)


h1 = House ('ЖК Горский', 18)
h2 = House ('Домик в деревне', 2)
print ('Название:', str (h1), ', количество этажей ', len (h1))
print ('Название:', str (h2), ', количество этажей ', len (h2))
