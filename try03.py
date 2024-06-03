import numpy as np
import matplotlib.pyplot as plt
import scipy as sc

phase01 = 'data/test_file_250424_1.bin'
phase02 = 'data/test_file_250424_2.bin'

data01 = np.fromfile(phase01,dtype=np.complex64)
data02 = np.fromfile(phase02,dtype=np.complex64)

time01 = np.zeros(30)
# time01 = np.arange(len(data01))
# time02 = np.arange(len(data02))
# Получаем мнимую часть комплексных чисел
imaginary_parts01 = np.imag(data01)
real_parts1 = np.real(data01)
imaginary_parts02 = np.imag(data02)
real_parts2 = np.real(data02)

sr=192000
phase2 = np.zeros(30)
phase1 = np.zeros(30)

# print(len(imaginary_parts01))
data1 = np.zeros(30)
data2 = np.zeros(30)

for i in range(30):

    time01[i] = i

    data1[i] = data01[i*sr]
    data2[i] = data02[i*sr]

for j in range(30):
    phase1[j] = imaginary_parts01[j*sr]
    phase2[j] = imaginary_parts02[j*sr]

plt.plot(time01, data1, marker='o')
plt.xlabel('Время')
plt.ylabel('Значение')
plt.title('Лул')
plt.grid(True)

plt.plot(time01, data2, marker='o')
plt.xlabel('Время')
plt.ylabel('Значение')
plt.title('Лул')
plt.grid(True)

plt.plot(time01, phase1, marker='o')
plt.xlabel('Время')
plt.ylabel('Фаза')
plt.title('Первый файл')
plt.grid(True)


plt.plot(time01, phase2, marker='o')
plt.xlabel('Время')
plt.ylabel('Фаза')
plt.title('Первый файл')
plt.grid(True)
plt.show()

# imaginary_parts02 = np.imag(data02)

# # Строим график
# plt.plot(time02, imaginary_parts02, marker='o')
# plt.xlabel('Время')
# plt.ylabel('Фаза')
# plt.title('Второй файл')
# plt.grid(True)
# plt.show()