# Input S.P , C.P. Find whether a person has gained profit, loss or no profit no loss

class find:
    def input(self):
        self.sp = int(input("Enter S.P : "))
        self.cp = int(input("Enter C.P : "))
    def cal(self):
        if(self.sp>self.cp):
            profit = ((self.sp - self.cp)/self.cp) * 100
            print("Profit : ", profit)
        else:
            loss = ((self.cp - self.sp)/self.cp) * 100
            print("Loss : ", loss)
x = find()
x.input()
x.cal()