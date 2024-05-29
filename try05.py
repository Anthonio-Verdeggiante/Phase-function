import numpy as np
import matplotlib.pyplot as plt

phase01 = 'test_ch1_5MHz_230524.bin'
phase02 = 'test_ch1_5MHz_24Kh.bin'

data01 = np.fromfile(phase01,dtype=np.complex64)
data02 = np.fromfile(phase02,dtype=np.complex64)

points = 192000

