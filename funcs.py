
def myfunc():
    print("My function")

myfunc()



class MyClass:
    def myfunc(self, arg1):
         print("MyClass f1", arg1)

    def myfunc2(self, arg1):
        print("MyClass f2", arg1)

class MyClass2:
    def myfunc2(self, arg1):
        print("MyClass2 f2", arg1)

class MyClass3(MyClass, MyClass2):
    def myfunc3(self, arg1):
        super().myfunc(arg1)
        super().myfunc2(arg1)
        MyClass2.myfunc2(self,arg1)


c = MyClass3()
c.myfunc3(10)
