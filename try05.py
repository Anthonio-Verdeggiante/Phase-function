import numpy as np
import matplotlib.pyplot as plt

phase01 = 'data/test_ch1_5MHz_230524.bin'
phase02 = 'data/test_ch1_5MHz_24Kh.bin'

data01 = np.fromfile(phase01,dtype=np.complex64)
data02 = np.fromfile(phase02,dtype=np.complex64)

points = 24000

a = 48

im_data1 = np.imag(data01)
re_data1 = np.real(data01)

im_data2 = np.imag(data02)
re_data2 = np.real(data02)

phase1 = np.zeros(a)
phase2 = np.zeros(a)

time = np.zeros(len)

for i in range(len(phase1)):

    phase1[i] = np.arctan(im_data1[i*points]/re_data1[i*points])
    time[i] = i/a

for i in range(a):

    phase2[i] = np.arctan(im_data2[i*points]/re_data2[i*points])


plt.figure()
plt.plot(time,phase1, marker='.')
plt.xlabel('Время')
plt.ylabel('Значение')
plt.grid(True)


plt.figure()
plt.plot(time, phase2, marker='.')
plt.xlabel('Время')
plt.ylabel('Значение')
plt.grid(True)
plt.show()