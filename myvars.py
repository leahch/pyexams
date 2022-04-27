

r = "rm"
print(r)

def f1() :
    _r = 10
    # def finternal():
    #     r = "ri"
    #     print(r)
    finternal = lambda i : _r * i
    print(finternal(2))
    _r = 11
    print(finternal(2))
    _r = 12
    print(finternal(2))

f1()
print(r)
