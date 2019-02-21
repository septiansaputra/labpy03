print (' Bilangan acak yang lebih kecil dari 0.5')
import random
n = int (input("masukan nilai N : "))
a = 0
for i in range(n):
    a+= 1
    b = random.uniform(.0, .5)
    print('data ke:', a, '-->', b)
print("selesai")

