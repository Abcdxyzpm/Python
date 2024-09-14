s = 0
for i in range(1,5):
    s += i
print(s)

sum = 0
for j in range(100,500):
    tem = j
    k = j % 2
    if(k == 0):
        sum += tem
print(sum)

# Factoeial 
#factorial 0 = 1
#factorial 5 = 120
#factorial 6 = f5 * 6
#factorial 7 = f6 * 7
#factorial 8 = f7 * 8
a1 = 5*4*3*2*1
print(a1)
num = 5
fact = 1
for b in range(1,num+1):
    fact *= b
print(fact)