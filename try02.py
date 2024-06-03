import numpy as np
import matplotlib.pyplot as plt
import scipy as sc

phase01 = 'data/test_ch1_5MHz_2305241.bin'
phase02 = 'data/test_file_250424_2.bin'

data01 = np.fromfile(phase01,dtype=np.complex64)
data02 = np.fromfile(phase02,dtype=np.complex64)
# a=len(data01)

sr=192000
b=5
c=100
a=int(b*c)

# time01 = np.arange(len(data01))
# time02 = np.arange(len(data02))
# Получаем мнимую часть комплексных чисел
imaginary_parts01 = np.imag(data01)
real_parts1 = np.real(data01)
imaginary_parts02 = np.imag(data02)
real_parts2 = np.real(data02)
phase2 = np.zeros(300)
phase1 = np.zeros(a)
time01 = np.zeros(a)
print(len(imaginary_parts01))
data1 = np.zeros(a)
data2 = np.zeros(60)
offset=sr*3
freq=5000000

data11 = np.zeros(a)
data22 = np.zeros(30)
data111 = np.zeros(30)
time=np.zeros(a)
print(len(data01)/sr)
for i in range(a):

    phase1[i] = np.arctan(imaginary_parts01[int(i*sr/b)]/real_parts1[int(i*sr/b)])
    # phase2[i] = np.arctan(imaginary_parts02[i*sr]/real_parts2[i*sr])
    

    time01[i] = i

    # data1[i] = data01[i*19200]
    # data2[i] = data02[int(i*sr/30)]

    # data11[i] = data01[i*sr]*np.cos(freq*i*sr)
    # data111[i] = -data01[i*sr]*np.sin(freq*i*sr)
    # phase1[i] = np.arctan(data111[i]/data11[i])
# for i in range(60):
#     data2[i] = data02[int(i*sr/30)]
#     time[i]=i/60
plt.figure()
plt.plot(time01, data1, marker='.')
plt.xlabel('Время')
plt.ylabel('Значение')
plt.grid(True)

plt.figure()
plt.plot(time01,phase1, marker='.')
plt.xlabel('Время')
plt.ylabel('Значение')
plt.grid(True)
plt.show()
# plt.plot(time01, , marker='o')
# plt.xlabel('Время')
# plt.ylabel('Фаза')
# plt.title('Первый файл')
# plt.grid(True)


# plt.plot(time01, phase2, marker='o')
# plt.xlabel('Время')
# plt.ylabel('Фаза')
# plt.title('Первый файл')
# plt.grid(True)
# plt.show()

# imaginary_parts02 = np.imag(data02)

# # Строим график
# plt.plot(time02, imaginary_parts02, marker='o')
# plt.xlabel('Время')
# plt.ylabel('Фаза')
# plt.title('Второй файл')
# plt.grid(True)
# plt.show()