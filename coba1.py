'''
A = 0
for S in range(1, 4, 1):
    A = A+3*S
print(S, "\t", A)


for i in range(1, 7):
    for k in range(5, -4 , -1):
        print(k, '\t', end="")
    print()
'''

t = int(input())
for i in range(1,t+1):
    for k in range(t-i, 0,-2):
        print(" ",end=" ")
    for j in range(i,0,-2):
        print('$',end= " ")
    print()
            
