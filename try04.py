import numpy as np
import matplotlib.pyplot as plt
import scipy as sc

phase01 = 'test_ch1_5MHz_230524.bin'
phase02 = 'test_ch1_5MHz_24Kh.bin'

data01 = np.fromfile(phase01,dtype=np.complex64)
data02 = np.fromfile(phase02,dtype=np.complex64)
# a=len(data01)

sr=24000
a=100
b=210

imaginary_parts01 = np.imag(data01)
real_parts1 = np.real(data01)

imaginary_parts02 = np.imag(data02)
real_parts2 = np.real(data02)

phase2 = np.zeros(b)
phase1 = np.zeros(a)

time01 = np.zeros(a)

print(len(imaginary_parts01))

data1 = np.zeros(a)
data2 = np.zeros(b)

offset=sr*3
freq=5000000

data11 = np.zeros(a)
data22 = np.zeros(30)
data111 = np.zeros(30)
time=np.zeros(b)

print(len(data01)/sr)

for i in range(100):

    phase1[i] = np.arctan(imaginary_parts01[i*2400]/real_parts1[i*2400])
    
    

    time01[i] = i/10


for i in range(210):

    phase2[i] = np.arctan(imaginary_parts02[i*2400]/real_parts2[i*2400])
    
    data2[i]=data02[i*2400]

    time[i] = i/10


# for i in range(60):
#     data2[i] = data02[int(i*sr/30)]
#     time[i]=i/60

inv_phase1 = np.zeros(a)
for i in range(len(phase1)):
    inv_phase1[i] = (-1)*phase1[i]


plt.figure()
plt.plot(time,data2, marker='.')
plt.xlabel('Время')
plt.ylabel('Значение')
plt.grid(True)


plt.figure()
plt.plot(time01,inv_phase1, marker='.')
plt.xlabel('Время')
plt.ylabel('Значение')
plt.grid(True)


det_phase1 = np.zeros(a)

for i in range(len(phase1)):
    det_phase1[i] = phase2[i] + inv_phase1[i]


plt.figure()
plt.plot(time01,det_phase1, marker='.')
plt.xlabel('Время')
plt.ylabel('Значение')
plt.grid(True)
plt.show()