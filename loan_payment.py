class loan():
    def __init__(self,loan,rate,m):
        self.loan = loan
        self.rate = rate
        self.m = m
    def total(self):
        loan = self.loan

        top_half=(self.rate*(1+self.rate)**self.m)

        bottom_half=(1+self.rate)**self.m - 1

        total = loan * (top_half/bottom_half)
        return total

my_loan = loan(10,1,10)
print("monthly payment needed for loan is ", int(my_loan.total()))


