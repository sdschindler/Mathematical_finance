#options payoff modelling



def optPayoff():
    optype = input('Enter the option type (C/P): ')
    K = int(input('Enter the excersie price: '))
    S = int(input('Enter the stock price: '))

    if optype == 'C':
        payoff = max(0,(S-K))
    elif optype == 'P':
        payoff = max(0,(K-S))
    print('Payoff is: ', payoff)

optPayoff()
