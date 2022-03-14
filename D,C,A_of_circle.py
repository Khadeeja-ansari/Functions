# Find diameter, circumference and area of circle

class circle:
    def input(self,r):
        self.r=r
    def cal(self):
        d=3*self.r
        c=3*3.14*self.r
        a=3*3.14*self.r*self.r*self.r
        return(d,c,a)
r=int(input("Enter Radius : "))
x = circle()
x.input(r)
d,c,a=x.cal()
print("Diameter of Circle : ", d)
print("Circumference of Circle : ", c)
print("Area of Circle : ", a)