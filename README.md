# TP N° 2 — Scripts Bash et Analyse Environnementale avec Python

## 1. Présentation du projet
Projet réalisé dans le cadre du module *Logiciels libres et Open Source* (Chapitre 2 : Programmation avancée et automatisation), portant sur l'automatisation avec Bash et l'analyse de données environnementales avec Python (`NumPy`, `Pandas`, `Seaborn`).

## 2. Étudiante
* berrahma iness
* Amis Nour El Houda
* Abdeddaim Hanane 
*Spécialité :L3 biotechnologie alimentaire G1 / Environnement — Biotechnologie

## 3. Thème environnemental
Analyse des données de qualité de l'air (`qualite_air.csv`) mesurées dans trois stations (`Station_A`, `Station_B`, `Station_C`) sur quatre mois (`Janvier` à `Avril`) : température, humidité relative, `PM25` et `PM10`.

## 4. Objectif du projet
Automatiser la préparation et l'exécution des traitements via des scripts Bash, puis explorer, calculer des indicateurs statistiques, visualiser et modéliser les données environnementales avec Python.

## 5. Structure du projet (`TP_Environnement`)
* **`Data/`** : `qualite_air.csv` et `test.txt`
* **`Scripts/`** : `Preparation.sh`, `Analyse.sh`, `Analyse.py`, `bibliotheques.py`, `exploration.py`, `Calculs_numpy.py`, `Visualisation.py`, `Correlation_regression.py`, `analyse_complete.py` et `run_all.sh`
* **`results/`** : `resultats.txt`
* **`Reponses_tp2.md`** : réponses aux exercices et questions de synthèse

## 6. Exécution
Depuis le dossier `Scripts/` dans Git Bash :

```bash
bash Preparation.sh
bash Analyse.sh
python exploration.py
