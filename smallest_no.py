# Find smallest of 3 numbers

class small:
    def input(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def cal(self):
        if self.a<self.c and self.a<self.b:
            return(self.a)
        elif self.b<self.a and self.b<self.c:
            return(self.b)
        else:
            return(self.c)
a=int(input("Enter I number : "))
b=int(input("Enter II number : "))
c=int(input("Enter III number : "))
x = small()
x.input(a,b,c)
d=x.cal()
print("Smallest of 3 number : ",d)