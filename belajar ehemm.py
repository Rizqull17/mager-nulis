'''
#belajar sorting dalam bubble
data = [3,7,1,2,9,5,67,45,76,31,99,95,90]
print(len(data))
def bubbleSort(data):
    for i in range (len(data)-1,0,-1):
        print("langkah")
        for j in range(0,len(data)-1):
            if (data[j] > data[j+1]):
                data[j],data[j+1] = data[j+1],data[j]
        print(data) 
bubbleSort(data)

#belajar sorting dalam selection
data1 = [3,6,1,8,9,12,33,43,15,91,43]
def selectionSort(data):
    print("data awal  \n",data)
    langkah = 0
    for i in range(len(data)-1,0,-1):
        print("langkah ke-",langkah)
        m=0

        for j in range(1,i+1):
            if data[j]> data[m]:
                m = j
        temp = data[i]
        data[i]=data[m]
        data[m]= temp
        
        langkah+=1
        print(data)
selectionSort(data1)

#belajar stack
tumpukan = [1,2,3,4,5,6]
print('data sekarang : ',tumpukan)
tumpukan.append(7)
print('data masuk:', 7)
tumpukan.append(8)
print('data masuk: ',8)

out = tumpukan.pop()
print('data keluar: ',out)
print('data sekarang : ',tumpukan)
'''
#belajar antrian quewing