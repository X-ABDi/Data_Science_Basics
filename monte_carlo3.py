import monte_carlo1 as mn1
import matplotlib.pyplot as plt
import numpy as np

def sim_Ntime(N, n):
    result = list()
    for _ in range(N):
        result.append(mn1.total_earning(n))
    result.sort()    
    return result

result1 = sim_Ntime(100000, 10)
result2 = sim_Ntime(100000, 25)
result3 = sim_Ntime(100000, 100)
result4 = sim_Ntime(100000, 1000)
new_result1 = [0]*21
new_result2 = [0]*51
new_result3 = [0]*201
new_result4 = [0]*2001
for i in range (100000):
    new_result1[result1[i]+10] += 1
    result1[i] = result1[i]/float(10)
for i in range (100000):
    new_result2[result2[i]+25] += 1
    result2[i] = result2[i]/float(25)
for i in range (100000):
    new_result3[result3[i]+100] += 1
    result3[i] = result3[i]/float(100)
for i in range (100000):
    new_result4[result4[i]+1000] += 1
    result4[i] = result4[i]/float(1000)


x1 = np.array(list(i for i in range(-10, 11)))
x2 = np.array(list(i for i in range(-25, 26)))
x3 = np.array(list(i for i in range(-100, 101)))
x4 = np.array(list(i for i in range(-1000, 1001)))
plt.plot(x1, new_result1, 'r', x2, new_result2, 'b', x3, new_result3, 'g', x4, new_result4, 'p')
# plt.plot(x, new_result)
plt.show()