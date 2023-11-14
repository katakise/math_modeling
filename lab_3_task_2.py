# from lab_3_task_1 import uscorenie_svopadnogo_padenia as g
import numpy as np 

h = 100
alfa = np.pi / 3
beta = 30
g = 5

v = np.sqrt(g* h * np.tan(beta)**2 / 2 * np.cos(alfa)**2 * (1- 0.5) )
print(v)