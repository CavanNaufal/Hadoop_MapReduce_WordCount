import matplotlib.pyplot as plt
import numpy as np

# Line plot
sizes = [1, 100, 200, 500, 1000]
python_times = [0.137, 27.021, 42.617, 243.039, 1905.303]
hadoop_times = [30.242, 62.245, 71.460, 93.246, 197.669]
ratios = [python_time / hadoop_time for python_time, hadoop_time in zip(python_times, hadoop_times)]

plt.figure(figsize=(12, 6))  # Adjust the figure size as needed

plt.subplot(121)
plt.plot(sizes, python_times, marker='o', label='Python (s)')
plt.plot(sizes, hadoop_times, marker='o', label='Hadoop (s)')
plt.xlabel('Ukuran (MB)')
plt.ylabel('Waktu (s)')
plt.title('Waktu Eksekusi Python dan Hadoop')
plt.grid(True)
plt.legend()

# Bar plot
plt.subplot(122)
bar_width = 0.25
index = np.arange(len(sizes))

bar1 = plt.bar(index, python_times, bar_width, label='Python (s)')
bar2 = plt.bar(index + bar_width, hadoop_times, bar_width, label='Hadoop (s)')
plt.bar(index + 2*bar_width, ratios, bar_width, label='Ratio')

plt.xlabel('Ukuran (MB)')
plt.ylabel('Waktu (s) / Rasio')
plt.title('Waktu Eksekusi Python, Hadoop, dan Rasio')
plt.xticks(index + bar_width, sizes)
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
