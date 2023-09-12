def VFaceval(Fb,rb,Tb):
    return Fb / ((1+rb)**Tb)

print(VFaceval(1000,0.015,4))


def VCouponval(c,i,n):
    ans=0
    for k in range(0,(n)):
        k +=1
        ans += (float(c)/((1+float(i))**k))
        print('Coupon paayment: ',ans)
print(VCouponval(25,0.015,4))
