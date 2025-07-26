import numpy as np
import similaritymeasures
import matplotlib.pyplot as plt

x = np.random.random(100)
y = np.random.random(100)
exp_data = np.zeros((100, 2))
exp_data[:, 0] = x
exp_data[:, 1] = y

x = np.random.random(100)
y = np.random.random(100)
num_data = np.zeros((100, 2))
num_data[:, 0] = x
num_data[:, 1] = y

pcm = similaritymeasures.pcm(exp_data, num_data)

df = similaritymeasures.frechet_dist(exp_data, num_data)

area = similaritymeasures.area_between_two_curves(exp_data, num_data)

cl = similaritymeasures.curve_length_measure(exp_data, num_data)

dtw, d = similaritymeasures.dtw(exp_data, num_data)

mae = similaritymeasures.mae(exp_data, num_data)

mse = similaritymeasures.mse(exp_data, num_data)

print(pcm, df, area, cl, dtw, mae, mse)

plt.figure()
plt.plot(exp_data[:, 0], exp_data[:, 1])
plt.plot(num_data[:, 0], num_data[:, 1])
plt.show()
