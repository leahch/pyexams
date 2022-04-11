
class Ball:
    color = "red"
    def __init__(self, col):
        self.color = col
 

# Calc2(10)





ball1 = Ball("gray")
print(ball1.color)

ball2 = Ball("yellow")
ball3 = Ball("black")
#ball2.color = "yellow"
print(ball2.color)
print(ball3.color)

c1 = Calc(10)
print(c1.a1)
print(c1.inc(100))
print(c1.a1)
print(c1.inc())
print(c1.a1)

c2 = Calc(10)
print(c2.inc(c1.a1))
print(c2.a1)

def ffff(aaa):
    pass

class Calc:
    def __init__(self, aaaa):
        self.a1 = aaaa
    
    def inc(self, i=1):
        self.a1 += i
        return self.a1
        
class Calc2(Calc):
    def dec(self, i=1):
        self.a1 -= i
        return self.a1

c3 = Calc2(10)
c3.inc()
c3.dec(30)
print(c3.a1)



