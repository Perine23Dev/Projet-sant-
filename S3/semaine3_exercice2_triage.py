# ============================================================
# AKIENI ACADEMY — Projet Santé Publique
# Semaine 3 — Exercice 2 : Triage Patient Urgences CHU Brazzaville
# ============================================================

print("=== SYSTEME DE TRIAGE — URGENCES CHU BRAZZAVILLE ===")
print("Protocole Manchester adapte — DSS Congo 2026")
print()

# -------------------------------------------------
# SAISIE DES DONNEES
# -------------------------------------------------

nom_patient = input("Nom du patient : ")
age_patient = int(input("Age (annees) : "))
temperature = float(input("Temperature (degres C, ex: 38.4) : "))
spo2 = float(input("Saturation O2 en % (ex: 96.0) : "))
tension_syst = int(input("Tension systolique en mmHg (ex: 135) : "))
douleur = int(input("Douleur /10 (0=aucune, 10=insupportable) : "))

# -------------------------------------------------
# VALIDATION DES DONNEES
# -------------------------------------------------

if age_patient < 0 or age_patient > 120:
    print("ERREUR : Age invalide — verifier la saisie")

if temperature < 35.0 or temperature > 43.0:
    print("ERREUR : Valeur de temperature impossible — verifier la saisie")

if spo2 < 50.0 or spo2 > 100.0:
    print("ERREUR : SpO2 hors plage — verifier le capteur")

if tension_syst < 50 or tension_syst > 250:
    print("ERREUR : Tension hors plage — verifier le brassard")

if douleur < 0 or douleur > 10:
    print("ERREUR : Douleur doit etre entre 0 et 10")

# -------------------------------------------------
# TRIAGE
# -------------------------------------------------

if temperature > 39.5 or spo2 < 90 or tension_syst > 180:

    niveau_triage = "1 — IMMEDIAT"
    couleur_triage = "[ROUGE]"
    delai_pec = "0 minute"
    action_triage = "Medecin present immediatement — code ROUGE active"

elif temperature > 38.5 or spo2 < 94 or tension_syst > 140:

    niveau_triage = "2 — URGENT"
    couleur_triage = "[ORANGE]"
    delai_pec = "10 minutes"
    action_triage = "Appel medecin senior"

elif temperature > 37.5 or douleur > 6:

    niveau_triage = "3 — URGENT DIFFERE"
    couleur_triage = "[JAUNE]"
    delai_pec = "30 minutes"
    action_triage = "Infirmier — surveillance"

else:

    niveau_triage = "4 — MOINS URGENT"
    couleur_triage = "[VERT]"
    delai_pec = "120 minutes"
    action_triage = "File d'attente standard"

# -------------------------------------------------
# MOTIF PRINCIPAL
# -------------------------------------------------

if temperature > 39.5:
    motif = f"Temperature {temperature} C > seuil 39.5 C"

elif spo2 < 90:
    motif = f"SpO2 {spo2}% < seuil 90%"

elif tension_syst > 180:
    motif = f"Tension {tension_syst} mmHg > seuil 180"

elif temperature > 38.5:
    motif = f"Temperature {temperature} C > seuil 38.5 C"

elif spo2 < 94:
    motif = f"SpO2 {spo2}% < seuil 94%"

elif tension_syst > 140:
    motif = f"Tension {tension_syst} mmHg > seuil 140"

elif temperature > 37.5:
    motif = f"Temperature {temperature} C > seuil 37.5 C"

elif douleur > 6:
    motif = f"Douleur {douleur}/10 > seuil 6"

else:
    motif = "Tous les parametres sont normaux"

# -------------------------------------------------
# ETAT DES PARAMETRES
# -------------------------------------------------

if temperature > 39.5:
    etat_temp = "[ANORMAL — > 39.5]"
elif temperature > 38.5:
    etat_temp = "[ANORMAL — > 38.5]"
elif temperature > 37.5:
    etat_temp = "[SURVEILLANCE]"
else:
    etat_temp = "[NORMAL]"

if spo2 < 90:
    etat_spo2 = "[CRITIQUE]"
elif spo2 < 94:
    etat_spo2 = "[ANORMAL]"
else:
    etat_spo2 = "[NORMAL]"

if tension_syst > 180:
    etat_tension = "[CRITIQUE]"
elif tension_syst > 140:
    etat_tension = "[ANORMAL]"
else:
    etat_tension = "[NORMAL]"

if douleur > 6:
    etat_douleur = "[ELEVEE]"
else:
    etat_douleur = "[NORMAL]"

# -------------------------------------------------
# AFFICHAGE
# -------------------------------------------------

print()
print("=" * 55)
print(f" RESULTAT TRIAGE — {nom_patient.upper()}")
print("=" * 55)

print(" PARAMETRES VITAUX")
print(f" Temperature     : {temperature} C      {etat_temp}")
print(f" Saturation O2   : {spo2} %      {etat_spo2}")
print(f" Tension systol. : {tension_syst} mmHg   {etat_tension}")
print(f" Douleur         : {douleur}/10      {etat_douleur}")

print("-" * 55)

print(f" NIVEAU DE TRIAGE : {niveau_triage}")
print(f" COULEUR          : {couleur_triage}")
print(f" PRISE EN CHARGE  : {delai_pec}")
print(f" ACTION           : {action_triage}")

print("-" * 55)

print(f" Motif principal : {motif}")

print("=" * 55)