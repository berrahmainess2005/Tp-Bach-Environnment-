import numpy as np
import pandas as pd

data = pd.read_csv("../../qualite_air.csv")
pm25 = np.array(data["PM25"])

print("Moyenne :", np.mean(pm25))
print("Minimum :", np.min(pm25))
print("Maximum :", np.max(pm25))
print("Ecart-type :", np.std(pm25))
