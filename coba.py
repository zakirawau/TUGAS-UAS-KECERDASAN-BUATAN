import skfuzzy as fuzz
import numpy as np

x = np.arange(0, 11, 1)
low = fuzz.trimf(x, [0, 0, 5])

print("Membership Function 'Low':", low)