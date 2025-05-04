from random import randint
class Field:
    def __init__(self,size,hares):
        self.size = size
        self.hares = []
        for _ in range(hares):
            cords = (1,1)
            while cords == (1,1):
                cords = (randint(1,self.size),randint(1,self.size))
                for i in self.hares:
                    if i == cords:
                        cords = (1,1)
            self.hares.append((cords[0],cords[1]))
        self.field = self.__get_field()
        self.poz_tiger = (1,1)
        self.play = True
    def __get_field(self):
        field = {}
        for y in range(self.size):
            y += 1
            field[y] = ['🟩'] * self.size
            for x in range(self.size):
                x += 1
                for i in self.hares:
                    if i == (x, y):
                        field[y].pop(-x)
                        field[y].insert(x, '🟪')
        field[1].pop(-1)
        field[1].insert(0, '🟧')
        return field
    def show(self):
        for value,i in self.field.items():
            print(f'\n{value}',end=' '*int(len(list(str(self.size))) - len(list(str(value)))))
            for _ in i:
                print('',_,end='')
class Tigers(Field):
    def trac_down_prey(self):
        if self.poz_tiger[0] != 1 and self.poz_tiger[0] != tiger.size and self.poz_tiger[1] != 1 and self.poz_tiger[1] != tiger.size:
            poz = randint(1,8)
        elif self.poz_tiger[0] == 1 and self.poz_tiger[1] == 1:
            poz = randint(1, 3)
        elif self.poz_tiger[0] == tiger.size and self.poz_tiger[1] == tiger.size:
            poz = randint(5,7)
        elif self.poz_tiger[0] == 1 and self.poz_tiger[1] == tiger.size:
            poz = randint(3,5)
        elif self.poz_tiger[0] == tiger.size and self.poz_tiger[1] == 1:
            if randint(1,2) == 1:
                poz = randint(7,8)
            else:
                poz = 1
        else:
            if self.poz_tiger[0] == 1:
                poz = randint(1, 5)
            elif self.poz_tiger[0] == tiger.size:
                if randint(1,2) == 1:
                    poz = 1
                else:
                    poz = randint(5,8)
            elif self.poz_tiger[1] == 1:
                if randint(1,2) == 1:
                    poz = randint(1,3)
                else:
                    poz = randint(7,8)
            else:
                poz = randint(3,7)
        if poz == 1:self.poz_tiger = (self.poz_tiger[0],self.poz_tiger[1]+1)
        if poz == 2: self.poz_tiger = (self.poz_tiger[0]+1, self.poz_tiger[1]+1)
        if poz == 3: self.poz_tiger = (self.poz_tiger[0]+1, self.poz_tiger[1])
        if poz == 4: self.poz_tiger = (self.poz_tiger[0]+1, self.poz_tiger[1]-1)
        if poz == 5: self.poz_tiger = (self.poz_tiger[0], self.poz_tiger[1]-1)
        if poz == 6: self.poz_tiger = (self.poz_tiger[0]-1, self.poz_tiger[1]-1)
        if poz == 7: self.poz_tiger = (self.poz_tiger[0]-1, self.poz_tiger[1])
        if poz == 8: self.poz_tiger = (self.poz_tiger[0]-1, self.poz_tiger[1]+1)
        self.field = {}
        for _ in range(1,self.size+1):
            self.field[_] = []
            for y in range(self.size):
                y += 1
                self.field[y] = ['🟩'] * self.size
                for x in range(self.size):
                    for i in self.hares:
                        if i == (x+1,y):
                            self.field[y].pop(-x)
                            self.field[y].insert(x, '🟪')
                    if self.poz_tiger == (x+1,y):
                        self.field[y].pop(-x)
                        self.field[y].insert(x, '🟧')
    def check(self):
        for hare in self.hares:
            for approximately_x in range(-1,2):
                for approximately_y in range(-1,2):
                    if (self.poz_tiger[0]+approximately_x,self.poz_tiger[1]+approximately_y) == hare:
                        return True
        return False
    def attack_prey(self):
        if self.check():
            if randint(1,2) == 1:
                print('Заяц сбежал от тигра')
            else:
                print('Заяц... не смог')
            return False
        else:
            return True
    def run_home(self):
        self.field = {}
        for _ in range(1, self.size + 1):
            self.field[_] = []
            for y in range(self.size):
                y += 1
                self.field[y] = ['🟩'] * self.size
                for x in range(self.size):
                    for i in self.hares:
                        if i == (x + 1, y):
                            self.field[y].pop(-x)
                            self.field[y].insert(x, '🟪')
        self.field[1].pop(-1)
        self.field[1].insert(0, '🟧')
tiger = Tigers(8,2)
tiger.show()
print()
tiger.check()
while tiger.attack_prey():
    tiger.trac_down_prey()
    tiger.show()
    print()
tiger.run_home()
tiger.show()
print(tiger.hares)
