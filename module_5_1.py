class House:
    def __init__(self,name,number_of_floors):
        self.name=name                              # имя
        self.number_of_floors=number_of_floors      # кол-во этажей


    def go_to(self,new_floor):
            if new_floor <= self.number_of_floors:
               print("выбранный этаж : ")
               fl_ = (i for i in range(1, new_floor+1))   # печать этажей
               for i in fl_:
                   print(i)
            else:
                print(f" этажа {new_floor} не существует")


#   неправильный выбор этажей :
h1 = House('ЖК Горский', 18)
print(f'объект {h1.name}, этажность {h1.number_of_floors}')
h1.go_to(19)
print("_"*20)

h2 = House('Домик в деревне', 2)
print(f'объект {h2.name}, этажность {h2.number_of_floors}')
h2.go_to(10)
print("_"*20)

#   правильный выбор этажей :

h1 = House('ЖК Горский', 18)
print(f'объект {h1.name}, этажность {h1.number_of_floors}')
h1.go_to(15)
print("_"*20)

h2 = House('Домик в деревне', 2)
print(f'объект {h2.name}, этажность {h2.number_of_floors}')
h2.go_to(2)