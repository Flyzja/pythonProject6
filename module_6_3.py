class Horse():

    def __init__(self):
        super().__init__()
        self.x_distance = 0     # пройденный путь.
        self.sound = 'Frrr'     # звук, который издаёт лошадь.

    def run(self, dx):
        self.x_distance += dx        # изменение дистанции
        return self.x_distance               # self.x_distance

class Eagle:

    def __init__(self):
        self.y_distance = 0     # высота полета.
        self.sound = 'I train, eat, sleep, and repeat'     # звук, который издаёт орел.

    def fly(self, dy):
        self.y_distance += dy  # изменение дистанции
        return self.y_distance  # self.x_distance

class Pegasus(Horse, Eagle):

    def __init__(self):
        super().__init__()

    def move(self, dx, dy):     # изменения дистанции
        self.x_distance += dx
        self.y_distance += dy
        return self.run(self.x_distance), self.fly(self.y_distance)

    def get_pos(self):                  #полученная позиция
        return self.x_distance, self.y_distance

    def voice(self):            #голос
        print(self.sound)



p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())
p1.voice()

print(Pegasus.mro())
