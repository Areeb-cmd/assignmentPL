#method overriding
class vehical:
    def move(self):
        print("vehicle is moving")
class car(vehical):
    def move(self):
        print(" driving on the road ")
class cycle(vehical):
    def move(self):
        print("pedalling on the road")
c=car()
b=cycle()
c.move()
b.move()