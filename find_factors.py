# Input a number and find its factors 

class factors:
    def input(self,n):
        self.n=n
    def cal(self):
        print("Factors are : ")
        for i in range(1,n+1):
            if(n%i==0):
                print(i)
n = int(input("Enter a number : "))
x = factors()
x.input(n)
x.cal()