#! /usr/bin/env python

import numpy as np # short name saves typing
import matplotlib.pyplot as plt

plt.subplot(1, 2, 1)
x = np.arange(-np.pi, np.pi, 0.01)
y_sin = np.sin(x)
y_sin2 = np.sin(x) ** 2
y_cos = np.cos(x)

plt.plot(x, y_sin, "r", label = "sine")
plt.plot(x, y_sin2, "g", label = "sine squared")
plt.plot(x, y_cos, "b", label = "cosine")

plt.legend(loc = "lower left")

plt.subplot(1, 2, 2, polar=True)
r = np.arange(-np.pi, np.pi, 0.01)
theta_sin = np.sin(x)
theta_sin2 = np.sin(x) ** 2
theta_cos = np.cos(x)

plt.plot(x, theta_sin, "r", label = "sine")
plt.plot(x, theta_sin2, "g", label = "sine squared")
plt.plot(x, theta_cos, "b", label = "cosine")

plt.legend(loc = "lower left")


plt.show()
