import numpy as np
import matplotlib.pyplot as grafik

x1 = int(input('Masukan nilai x1  = '))
y1 = int(input('Masukan nilai y1  = '))
x2 = int(input('Masukan nilai x2  = '))
y2 = int(input('Masukan nilai y2  = '))

print('=====================================================')

x = x1
y = y1

if x1 == x2:
    titik_A = []
    titik_B = []
    for i in range(0, y2, 1):
        print('Garis yang di lewati oleh titik A da titik B yaitu : ', x, ',', y)
        titik_A.append(x)
        titik_B.append(y)
        y=y+1


elif y1 == y2:
    titik_A = []
    titik_B = []
    for i in range(0, x2, 1):
        print('Garis yang di lewati oleh titik A dan B yaitu : ', x, ',', y)
        titik_A.append(x)
        titik_B.append(y)
        x=x+1

else:
    titik_A = []
    titik_B = []
    m_gradiengaris = (y2 - y1) / (x2 - x1)
    print('Nilai Gradien Garis = ',m_gradiengaris)
    N = x2 - x1 + 1
    print('Nilai N = ',N)
    for i in range (0,N,1):
        nilai_y = m_gradiengaris * (x - x1) + y1
        ya = round(nilai_y)
        print('Garis yang di lewati oleh titik A da titik B yaitu : ', x,',', ya)
        titik_A.append(x)
        titik_B.append(ya)
        x+=1

grafik.title('Diagram Kartesius'"\n"'Algoritma Brute Force')
grafik.xlabel(titik_A)
grafik.ylabel(titik_B)
grafik.plot(titik_A,titik_B)
grafik.scatter(titik_A,titik_B)
grafik.grid()
grafik.show()