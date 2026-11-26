import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("../Results", exist_ok=True)

df = pd.read_csv("../Data/qualite_air.csv")
num_cols = df.select_dtypes(include="number").columns

summary_lines = []
summary_lines.append("=== RAPPORT D'ANALYSE ENVIRONNEMENTALE ===")
summary_lines.append(f"Dimensions : {df.shape[0]} lignes x {df.shape[1]} colonnes")
summary_lines.append("\nValeurs manquantes :")
summary_lines.append(df.isnull().sum().to_string())

if len(num_cols) > 0:
    summary_lines.append("\nStatistiques descriptives :")
    summary_lines.append(df[num_cols].describe().to_string())

    plt.figure(figsize=(8, 5))
    sns.histplot(df[num_cols[0]].dropna(), kde=True)
    plt.title(f"Distribution de {num_cols[0]}")
    plt.tight_layout()
    plt.savefig("../Results/analyse_distribution.png")
    plt.close()

if len(num_cols) >= 2:
    plt.figure(figsize=(8, 6))
    sns.heatmap(df[num_cols].corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Matrice de correlation")
    plt.tight_layout()
    plt.savefig("../Results/matrice_correlation.png")
    plt.close()

report_path = "../Results/rapport_analyse.txt"
with open(report_path, "w", encoding="utf-8") as f:
    f.write("\n".join(summary_lines))

print(f"Analyse terminee. Rapport enregistre dans {report_path}")
