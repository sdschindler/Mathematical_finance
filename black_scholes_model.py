import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
N = norm.cdf

def BS_CALL(S,K,T,r,sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/sigma * np.sqrt(T)
    d2 = d1 - sigma * np.sqrt(T)
    return S * N(d1) - K*np.exp(-r*T)*N(d2)

def BS_PUT(S,K,T,r,sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T)/sigma * np.sqrt(T)
    d2 = d1 - sigma * np.sqrt(T)
    return K*np.exp(-r*T)*N(-d2) - S*N(-d1)


K = 100
r = 0.1
T = 1
sigma = 0.3

S = np.arange(60,140,0.1)# array range
calls = [BS_CALL(s,K, T, r, sigma) for s in S] #array of series of option value
puts = [BS_PUT(s,K, T, r, sigma) for s in S] #array of series of option value
plt.plot(S,calls,label = 'Call value')
plt.plot(S,puts,label = 'put value')
plt.xlabel('Stock Price')
plt.ylabel('Option Value')
plt.title('Impact of BSM of S')
plt.legend()
