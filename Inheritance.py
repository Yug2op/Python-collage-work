class Parent:
    def parentfunc(self):
        print("This is parent function")

class Child (Parent):
    def childfunc(self):
        print("This is child function")
ch = Child()        
ch.parentfunc()