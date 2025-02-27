# 1. create a class create user defined function to check weather a string is palindrome or not.

class palindrom:
    def __init__(self,str):
         self.str = str
    def isplindrom (self):
        start = 0
        end = len(self.str) - 1
        while start <= end:
            if self.str [start] != self.str[end]:
                return False
            start +=1
            end -=1

        return True
str = input("Enter astring to check: ")    
pal = palindrom(str)
print (pal.isplindrom())

