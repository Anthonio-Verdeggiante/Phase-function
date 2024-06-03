import numpy as np
import matplotlib.pyplot as plt

phase01 = 'data/test_ch1_5MHz_2305241.bin'
# phase02 = 'data/test_ch1_5MHz_24Kh.bin'
phase02 = 'data/test_file_250424_2.bin'

data01 = np.fromfile(phase01,dtype=np.complex64)
data02 = np.fromfile(phase02,dtype=np.complex64)

points = 24000

a = 24

im_data1 = np.imag(data01)
re_data1 = np.real(data01)

im_data2 = np.imag(data02)
re_data2 = np.real(data02)

phase1 = np.zeros(a)
phase2 = np.zeros(a)

time = np.zeros(a)

# Расчет агрумента

for i in range(len(phase1)):

    phase1[i] = np.arctan(im_data1[i*points]/re_data1[i*points])
    time[i] = i

for i in range(a):

    phase2[i] = np.arctan(im_data2[i*points]/re_data2[i*points])

# График мнимой части от времени
im_data11 = np.zeros(a)
im_data22 = np.zeros(a)

for i in range(a):
    im_data11[i] = im_data1[i]*points

for i in range(a):
    im_data22[i] = im_data2[i]*points

plt.figure()
plt.plot(time,im_data11, marker='.')
plt.xlabel('Время')
plt.ylabel('Значение')
plt.grid(True)
plt.title('Мнимая часть. Файл 1')

plt.figure()
plt.plot(time, im_data22, marker='.')
plt.xlabel('Время')
plt.ylabel('Значение')
plt.grid(True)
plt.title('Мнимая часть. Файл 2')
plt.show()
# График аргумента от времени


plt.figure()
plt.plot(time,phase1, marker='.')
plt.xlabel('Время')
plt.ylabel('Значение')
plt.grid(True)
plt.title('Фаза. Файл 1')

plt.figure()
plt.plot(time, phase2, marker='.')
plt.xlabel('Время')
plt.ylabel('Значение')
plt.grid(True)
plt.title('Фаза. Файл 2')
plt.show()

### Продолжение кода - конформное отображение и детренд аргумента 
### Продолжение кода - конформное отображение и детренд аргумента 
### Продолжение кода - конформное отображение и детренд аргумента 

# Конформное отображение

re_data11 = np.zeros(a)
re_data22 = np.zeros(a)

for i in range(a):
    re_data11[i] = re_data1[i]*points

for i in range(a):
    re_data22[i] = re_data2[i]*points

plt.figure()
plt.plot(re_data11,im_data11, marker='.')
plt.xlabel('Время')
plt.ylabel('Значение')
plt.grid(True)
plt.title('Конформка. Файл 1')

plt.figure()
plt.plot(re_data22, im_data22, marker='.')
plt.xlabel('Время')
plt.ylabel('Значение')
plt.grid(True)
plt.title('Конформка. Файл 2')
plt.show()