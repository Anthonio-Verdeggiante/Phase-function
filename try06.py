import numpy as np
import matplotlib.pyplot as plt
import cmath

phase01 = 'data/test_ch1_5MHz_230524.bin'
phase02 = 'data/test_ch1_5MHz_24Kh.bin'

data01 = np.fromfile(phase01,dtype=np.complex64)
data02 = np.fromfile(phase02,dtype=np.complex64)

a = 192000

phase1 = np.zeros(a)
phase2 = np.zeros(a)
time = np.zeros(a)

for i in range(a):
    phase1[i] = cmath.phase(data01[i])
    time[i] = i

print(phase1)

plt.figure()
plt.plot(time,phase1, marker='.')
plt.xlabel('Время')
plt.ylabel('Значение')
plt.grid(True)
plt.show()

