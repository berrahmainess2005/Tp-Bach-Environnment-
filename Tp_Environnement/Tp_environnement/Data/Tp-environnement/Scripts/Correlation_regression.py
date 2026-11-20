import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("../../qualite_air.csv")
temperature = data["Temperature"].to_numpy()
pm25 = data["PM25"].to_numpy()

# 1. Calcul de correlation
correlation = np.corrcoef(temperature, pm25)[0, 1]
print("Coefficient de correlation :", correlation)

# 2. Modelisation par regression lineaire
a, b = np.polyfit(temperature, pm25, 1)
print("Coefficient a :", a)
print("Coefficient b :", b)

prediction = a * 25 + b
print("PM2.5 estimee pour 25 degres :", prediction)

# 3. Visualisation du modele
sns.regplot(
    x=temperature,
    y=pm25,
    ci=None
)
plt.title("Regression lineaire : Temperature et PM2.5")
plt.xlabel("Temperature (°C)")
plt.ylabel("PM2.5 (µg/m3)")
plt.show()
