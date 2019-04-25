class MyClass():
    def __init__(self,name="",age=0):
        self.name=name
        self.age=age
    def __del__(self):
        print("MyClass is delete.")

    def printf(self):
        print ('hello world, %s' %(self.name))

    def printf2(self):
        print ('hello world,' ,self.name)

    def printf3(self):
        print ('姓名:%s,年龄:%s' %(self.name,self.age))

myclass=MyClass("zzl")
myclass.printf()
myclass.printf2()

myclass3 = MyClass("zzl", "35")
myclass3.printf3()