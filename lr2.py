import threading
import numpy as np

def multiply(m1,m2,m3):
    temp = m3
    def calc(a, b, num):
        if num is 0:
            temp.append([])
            for i in range(3):
                temp[0].append(sum(a[0]*b[:,i]))
        if num is 1:
            temp.append([])
            for i in range(3):
                temp[1].append(sum(a[1]*b[:,i]))
        if num is 2:
            temp.append([])
            for i in range(3):
                temp[2].append(sum(a[2]*b[:,i]))
    for i in range(3):
        threading.Thread(target=calc, args=(m1, m2, i)).start()
    return temp

A = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
B = np.array([(9, 8, 7), (6, 5, 4), (3, 2, 1)])
C = []
print(multiply(A, B, C))