# Réponses — TP N° 2 : Scripts Bash et Analyse Environnementale (Python)

## Exercice 1 : Découverte de Bash et Git Bash
* **Intérêt des commandes Bash vs Explorateur Windows :** Les commandes Bash permettent d'automatiser les tâches répétitives, de manipuler rapidement les fichiers et dossiers, d'éviter les erreurs manuelles, d'enchaîner plusieurs opérations et de lancer directement des scripts Python.

## Exercice 2 : Création et exécution d'un script Bash
* **Différence entre exécution directe dans le terminal et script Bash :** Une commande exécutée directement s'applique immédiatement pour une action ponctuelle ou un test, alors qu'un script Bash regroupe plusieurs commandes dans un fichier (`.sh`) afin de les exécuter automatiquement, dans le même ordre et de manière reproductible.

## Exercice 3 : Automatisation de l'exécution d'un programme Python
* **Comment Bash automatise l'exécution de Python :** En appelant l'interpréteur Python (`python` / `python3`) à l'intérieur d'un script `.sh`, éventuellement accompagné de messages de suivi ou de création de dossiers, ce qui permet de lancer le traitement en une seule commande.
* **Application dans un laboratoire environnemental :** Automatiser chaque jour ou semaine l'importation des relevés de capteurs/stations, le calcul des indicateurs, la génération des graphiques et l'enregistrement des résultats dans un dossier dédié sans intervention manuelle répétitive.

## Exercice 4 : Préparation de l'environnement Python
1. **Qu'est-ce qu'une bibliothèque Python :** Un ensemble de fonctions, classes et outils prêts à l'emploi qui permettent de réaliser des tâches spécifiques sans tout programmer soi-même.
2. **Pourquoi utilise-t-on `import` :** Pour charger une bibliothèque ou un module dans le programme afin d'utiliser ses fonctions et objets.
3. **Différence entre Python et NumPy :** Python est le langage général avec ses structures de base (comme les listes), tandis que NumPy est une bibliothèque scientifique spécialisée dans les tableaux numériques performants et les calculs mathématiques/vectoriels.
4. **Rôle de Pandas dans l'analyse des données :** Importer des jeux de données (ex. CSV), les structurer sous forme de tableaux (`DataFrame`), les explorer, les nettoyer et calculer des résumés statistiques.
5. **Pourquoi utilise-t-on Seaborn :** Pour produire des visualisations statistiques claires et lisibles (histogrammes, boxplots, nuages de points, régressions) facilitant l'analyse des distributions et des relations entre variables.

## Exercice 5 : Création et exploration d'un jeu de données avec Pandas
Sur le jeu de données `qualite_air.csv` (3 stations, 4 mois) :
1. **Nombre de lignes :** 12 lignes d'observations.
2. **Nombre de colonnes :** 6 colonnes (`Station`, `Mois`, `Temperature`, `Humidite`, `PM25`, `PM10`).
3. **Variables quantitatives :** `Temperature`, `Humidite`, `PM25`, `PM10`.
4. **Variables qualitatives :** `Station`, `Mois`.
5. **Température maximale :** 26 °C (enregistrée à `Station_B` en `Avril`).
6. **Concentration maximale de PM2.5 :** 32 µg/m³ (enregistrée à `Station_C` en `Avril`).
7. **Valeurs manquantes :** Non, aucune valeur manquante (0).

## Exercice 6 : Calculs scientifiques avec NumPy
1. **Qu'est-ce qu'un tableau NumPy (`Array`) :** Une structure de données multidimensionnelle optimisée pour le calcul numérique, regroupant généralement des éléments de même type.
2. **Différence entre une liste Python et un tableau NumPy :** La liste Python accepte des types variés mais est moins adaptée aux calculs numériques massifs ; le tableau NumPy est plus rapide et permet des opérations mathématiques directes sur l'ensemble des éléments.
3. **Ce que représente l'écart-type :** La dispersion des valeurs autour de la moyenne ; un écart-type faible indique des valeurs proches de la moyenne, tandis qu'un écart-type élevé indique une plus grande variabilité.
4. **Importance des calculs statistiques en environnement :** Résumer de grands volumes de mesures, comparer des stations ou périodes, repérer des valeurs extrêmes/dépassements et appuyer l'interprétation scientifique.

## Exercice 7 : Visualisation des données avec Seaborn
* **A. Histogramme — Classe de PM2.5 la plus représentée :** La classe centrale des concentrations (autour de 15 à 22 µg/m³ sur l'ensemble des mesures) regroupe le plus grand nombre d'observations.
* **B. Boxplot :**
  1. **Station aux concentrations les plus élevées :** `Station_C` (valeurs comprises entre 20 et 32 µg/m³).
  2. **Station à la plus grande dispersion :** `Station_C` également (étendue de 12 µg/m³, de 20 à 32 µg/m³).
  3. **Intérêt du boxplot en environnement :** Il permet de visualiser rapidement la médiane, la dispersion (quartiles/étendue) et les valeurs atypiques pour comparer plusieurs stations ou périodes.
* **C. Nuage de points (Scatterplot) :**
  1. **Relation entre température et PM2.5 :** Une tendance globale plutôt croissante apparaît, mais elle varie selon les stations et les mois.
  2. **Points regroupés ou dispersés :** Les points sont relativement dispersés selon les stations plutôt que concentrés sur une droite étroite.
  3. **Peut-on conclure que la température provoque l'augmentation de PM2.5 :** Non, une observation graphique seule ne suffit pas à établir une relation de cause à effet.

## Exercice 8 : Corrélation et modélisation simple avec NumPy
1. **Ce que représente le coefficient `a` :** La pente de la droite de régression linéaire ($\text{PM2.5} = a \times \text{Température} + b$), indiquant la variation moyenne estimée de `PM2.5` lorsque la température augmente de 1 °C.
2. **Ce que représente le coefficient `b` :** L'ordonnée à l'origine, soit la valeur théorique estimée de `PM2.5` lorsque la température vaut 0 °C selon le modèle linéaire.
3. **Valeur estimée de PM2.5 pour 25 °C :** Calculée par `a * 25 + b` (environ **23,0 µg/m³** sur les 12 observations du TP).
4. **Corrélation implique-t-elle causalité :** Non ; une corrélation mesure une association statistique ou linéaire, pas nécessairement un lien de cause à effet.
5. **Autres variables environnementales influençant PM2.5 :** L'humidité relative, la vitesse et la direction du vent, les précipitations, les sources d'émission (trafic, industrie, chauffage) et les variations saisonnières.
6. ## Partie C — Exercice 9 : Automatisation complète avec Bash et Python
* **Chaîne automatisée (`analyse.sh`) :** Permet de créer automatiquement le dossier `results` (`mkdir -p ../results`), d'exécuter le script d'analyse Python (`exploration.py` / `analyse_complete.py`) et d'afficher des messages de suivi à chaque étape en une seule commande.
* **Enregistrement des résultats (`resultats.txt`) :** Le programme Python enregistre les statistiques descriptives et résumés dans `../results/resultats.txt` afin de conserver une trace exploitable sans ressaisie manuelle.

## Questions de synthèse
1. **Différence entre Bash et Python :** Bash est un interpréteur de commandes/shell orienté système, fichiers et automatisation de tâches/programmes, tandis que Python est un langage de programmation complet très adapté au traitement de données, aux calculs scientifiques et à la visualisation.
2. **Rôle de NumPy dans le traitement des données :** Fournir des tableaux numériques performants et des fonctions mathématiques/statistiques (moyenne, écart-type, corrélation, régression) rapides sur des données chiffrées.
3. **Pourquoi utiliser Pandas plutôt que traiter manuellement un fichier CSV :** Pandas automatise la lecture, l'indexation, le filtrage, la détection des valeurs manquantes et le calcul statistique sur des tableaux, évitant les erreurs et lenteurs du traitement manuel.
4. **Différence entre un histogramme et un boxplot :** L'histogramme montre la répartition/fréquence des valeurs d'une variable continue par classes (intervalles), tandis que le boxplot résume la distribution par la médiane, les quartiles, l'étendue/dispersion et les valeurs atypiques (pratique pour comparer plusieurs groupes).
5. **À quoi sert une matrice de corrélation :** À visualiser d'un coup d'œil les coefficients de corrélation linéaire entre toutes les paires de variables numériques afin d'identifier celles qui varient ensemble.
6. **Utilité de la régression linéaire :** Modéliser la relation linéaire entre une variable explicative et une variable cible afin d'analyser la tendance et d'estimer/prédire des valeurs.
7. **Association de Bash et Python pour automatiser un travail scientifique :** Bash orchestre l'environnement (dossiers, enchaînement des étapes, exécution répétée ou planifiée) et appelle les scripts Python qui réalisent le calcul, l'analyse et la génération des sorties.
8. **Pourquoi privilégier les logiciels libres et Open Source dans les laboratoires de recherche :** Ils offrent la transparence du code (reproductibilité scientifique), l'absence de coûts de licence bloquants, la pérennité des formats/outils et une large communauté scientifique active.

