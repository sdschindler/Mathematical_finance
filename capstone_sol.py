#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def findPayment(loan, r, m):
# Assumes: loan and r are floats, m an int
# Returns the monthly payment for a mortgage of size loan at a monthly rate of r fo
    return loan*((r*(1+r)**m)/((1+r)**m - 1))



class Mortgage(object):
# """Abstract class for building different kinds of mortgages"""
    def __init__(self, loan, annRate, months):
#"""Create a new mortgage, initialised by value returned by function findPayme
        self.loan = loan
        self.rate = annRate/12.0
        self.months = months
        self.paid = [0.0]
        self.owed = [loan]
        self.payment = findPayment(loan, self.rate, months)
        self.legend = None
#description of mortgage
    def makePayment(self):
# """Make a payment"""
        self.paid.append(self.payment)
        reduction = self.payment - self.owed[-1]*self.rate
        self.owed.append(self.owed[-1] - reduction)
    def getTotalPaid(self):
#"""Return the total amount paid so far"""
        return sum(self.paid)
    def __str__(self):
        return self.legend





# Classes for calculating TYPE 1 and TYPE 2
class Fixed(Mortgage):
# Inheriting mortgage class
    def __init__(self, loan, r, months):
        Mortgage.__init__(self, loan, r, months)
        self.legend = 'Fixed, ' + str(r*100) + '%'
class FixedWithPts(Mortgage):
## Inheriting mortgage class
    def __init__(self, loan, r, months, pts):
        Mortgage.__init__(self, loan, r, months)
        self.pts = pts
        self.paid = [loan*(pts/100.0)]
        self.legend = 'Fixed, ' + str(r*100) + '%, '\
+ str(pts) + ' points'





def compareMortgages(amt, years, fixedRate, pts, ptsRate):
    totMonths = years*12
    fixed1 = Fixed(amt, fixedRate, totMonths)
    fixed2 = FixedWithPts(amt, ptsRate, totMonths, pts)
    morts = [fixed1, fixed2]
    for m in range(totMonths):
        for mort in morts:
            mort.makePayment()
            for m in morts:
                print (m)
                print (' Total payments = Rs ' + str(int(m.getTotalPaid())))

compareMortgages(amt=1000000, years=30, fixedRate=0.07,pts = 10, ptsRate=0.07)