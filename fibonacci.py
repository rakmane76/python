#!/usr/bin/python3

def fib(max):
    a, b = 0, 1 
    while a < max:
        yield a 
        a, b = b, a + b 

glob = 100

class Fib :
    def __init__(self, max) :
        self.max = max

    def __iter__(self) :
        self.a = 0
        self.b = 1

        return(self)

    def __next__(self) :
        if self.a > self.max :
            raise StopIteration

        res = self.a
        self.a, self.b = self.b, self.a + self.b

        return res

    def geta(self) : 
        return self.a

    def getmax(self) : 
        return self.max

    def getglob(self) : 
        return glob

for i in fib(100) :
    print(i, end=' ')

print("\n ========================= \n")

#l = list(fib(50))
#print(l)

f = Fib(100)


for i in f :
    print(i, end=' ')
print("\n ========================= \n")

print(" f.a:{}".format(f.geta()))
print(" f.max:{}".format(f.getmax()))
print(" f.glob:{}".format(f.getglob()))
