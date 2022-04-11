
def f1():
    print("Без параметров")

def f2(param1, param2 = 123):
    print(param1, param2)
    pass

def f3( a, b,*c ):
    print(a,b,len(c), c)
    pass

def f4(**a):
    if len(a) == 1:
        print( a["a1"] )
    else:
        print( a )
    pass

def f5(a,b,c,d):
    pass

f1()
f2(10)
f2(param2=10,param1=11)

f3(1,2,3)

f4( a1=1123, a2=2 , a3=3)
f4( a1=1123)
print("-------------------------")
m1 = [11,22,33, 44]
print(m1)
f3(99, 88, *m1)








