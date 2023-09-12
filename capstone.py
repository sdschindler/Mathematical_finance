def findPayment(loan,r,m):
    top_half = r*(1+r)**m
    bottom_half = (1+r)**m - 1
    return loan * (top_half/bottom_half)

print("total payment needed for loan is ", findPayment(10,10,10))


class loan(object):
    def __init__(self,loan,annRate,months):
        self.loan = loan
        self.rate = annRate/12.0
        self.months = months
        self.paid = [0.0]
        self.owed = [loan]
        self.payment = findPayment(loan,self.rate,months)
        self.legend = None #description of mortgage
    def makePayment(self):
        self.paid.append(self.payment)
        print("paid is ", self.paid)
        reduction = self.payment - self.owed[-1]*self.rate
        print("self.paymeent is ",self.payment)
        print("self.rate is ",self.rate)
        print("self.owed[-1] is ",self.owed[-1])
        print("self.owed[-1]*self.rate is ", self.owed[-1]*self.rate)
        print("reduction is ",reduction)
        self.owed.append(self.owed[-1] - reduction)
        print("owed is ",self.owed)
    def getTotalPaid(self):
        return sum(self.paid)
    def __str__(self):
        return self.legend

class Fixed(loan):
    def __init__(self,loan,r,months):
