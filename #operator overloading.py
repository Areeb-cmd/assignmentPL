#operator overloading
class box:
    def __init__(self,weight):
        self.weight=weight
    def __add__(self, other):
        return self.weight+other.weight
b1=box(659)
b2=box(353)
print(b1+b2)