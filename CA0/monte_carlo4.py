import monte_carlo1 as mn1
import pandas as pd

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
for i in range (100000):
    new_result2[result1[i]+25] += 1
for i in range (100000):
    new_result3[result1[i]+100] += 1
for i in range (100000):
    new_result4[result1[i]+1000] += 1
    
new_results = [
    [10, 25, 100, 1000],
    new_result1,
    new_result2,
    new_result3, 
    new_result4
] 
# df = pd.DataFrame(new_results[1:], columns=new_results[0])
# df.to_csv('raw_results.csv', index=False)
    
expected_1 = 0
expected_2 = 0
expected_3 = 0
expected_4 = 0
stan_div1 = 0
stan_div2 = 0
stan_div3 = 0
stan_div4 = 0

for i in range (-10, 11):
    expected_1 += i*new_result1[i+10]
expected_1 = expected_1/float(100000) 
for i in range (-25, 26):
    expected_2 += i*new_result2[i+25]
expected_2 = expected_2/float(100000) 
for i in range (-100, 101):
    expected_3 += i*new_result3[i+100]
expected_3 = expected_3/float(100000) 
for i in range (-1000, 1001):
    expected_4 += i*new_result4[i+1000]
expected_4 = expected_4/float(100000) 

for i in range (-10, 11):
    stan_div1 += new_result1[i+10]*((i-expected_1)**2)  
stan_div1 = (stan_div1/float(100000))**0.5
for i in range (-25, 26):
    stan_div2 += new_result2[i+25]*((i-expected_2)**2)  
stan_div2 = (stan_div2/float(100000))**0.5
for i in range (-100, 101):
    stan_div3 += new_result3[i+100]*((i-expected_3)**2)  
stan_div3 = (stan_div3/float(100000))**0.5 
for i in range (-1000, 1001):
    stan_div4 += new_result4[i+1000]*((i-expected_4)**2)  
stan_div4 = (stan_div4/float(100000))**0.5

print(expected_1, "  ", stan_div1)
print(expected_2, "  ", stan_div2)
print(expected_3, "  ", stan_div3)
print(expected_4, "  ", stan_div4)