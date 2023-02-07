import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np

calibration_data = pd.read_excel('Interferometer.xlsx', usecols = 'D:I')
calibration_data.head()

def line(x, m, b):
    return m*x + b

M = calibration_data["M (micrometer Reading)"]
d = (calibration_data["delta d (nm)"]/1000)
derr = (calibration_data["d error"]/1000)

plt.errorbar(M, d, yerr=derr, ls="", marker=".")
plt.xlabel("M (Micrometer Reading) mm")
plt.ylabel("Path Difference (um)")

popt, pcov = curve_fit(line, M, d, p0=(-300/14, 300))
plt.plot(M, line(M, popt[0], popt[1]))
print(popt[0])
plt.show()

gas_data = pd.read_excel('GasCellData.xlsx', usecols='A:C')
