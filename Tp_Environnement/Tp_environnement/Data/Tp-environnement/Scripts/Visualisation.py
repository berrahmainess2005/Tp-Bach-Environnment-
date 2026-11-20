import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("../../qualite_air.csv")

# A. Histogramme
sns.histplot(data=data, x="PM25", bins=6)
plt.title("Distribution des concentrations PM2.5")
plt.xlabel("PM2.5 (ug/m3)")
plt.ylabel("Frequence")
plt.show()

# B. Diagramme en boite (Boxplot)
sns.boxplot(data=data, x="Station", y="PM25")
plt.title("Comparaison des PM2.5 par station")
plt.show()

# C. Nuage de points (Scatterplot)
sns.scatterplot(
    data=data,
    x="Temperature",
    y="PM25",
    hue="Station"
)
plt.title("Temperature et concentration PM2.5")
plt.show()
