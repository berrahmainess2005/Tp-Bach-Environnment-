#!/bin/bash

echo "=========================================="
echo "EXECUTION COMPLETE DU PROJET TP_ENVIRONNEMENT"
echo "=========================================="

bash preparation.sh
python3 bibliotheques.py
python3 exploration.py
python3 calculs_numpy.py
python3 correlation_regression.py
python3 visualisation.py
python3 analyse_complete.py

echo "=========================================="
echo "TOUTES LES ETAPES SONT TERMINEES AVEC SUCCES !"
echo "=========================================="
