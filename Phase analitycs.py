import numpy as np
import matplotlib.pyplot as plt
import scipy as sc


# print(data)
import struct

def parse_signal_file(test_file_250424_1):
    # Открываем файл в бинарном режиме
    with open('test_file_250424_1.bin', 'rb') as file:
        # Читаем данные из файла
        data = file.read()

  
    # Разбиваем данные на отдельные значения сигнала
    signal_values = []
    # Цикл по 4 байтам каждый (float32)
    for i in range(0, len(data), 4):
        
        # Читаем 4 байта и интерпретируем их как float32
        value = struct.unpack('f', data[i:i+4])[0]
        print(data)
        signal_values.append(value)

    return signal_values

def find_phase_data(signal_values):
    
    # Предположим, что фаза находится во второй половине данных
    # Может потребоваться изменить это, в зависимости от специфики данных
    phase_data = signal_values[len(signal_values)//2:]
    return phase_data

def plot_phase_vs_time(phase_data):
    time_steps = range(len(phase_data))

    plt.figure(figsize=(10, 6))
    plt.plot(time_steps, phase_data, marker='o', linestyle='-')
    plt.title('Dependence of Phase on Time')
    plt.xlabel('Time')
    plt.ylabel('Phase')
    plt.grid(True)
    plt.show()

# Путь к файлу с данными сигнала
file_path = 'signal_data.bin'

# Парсим файл с данными сигнала
signal_values = parse_signal_file(file_path)

# Находим данные о фазе
phase_data = find_phase_data(signal_values)

# Строим график зависимости фазы от времени
plot_phase_vs_time(phase_data)