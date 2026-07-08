# ============================================================
# AKIENI ACADEMY — Projet Santé Publique
# Semaine 2 — Exercice 3 : Rapport Comparatif Hôpitaux du Pool
# ============================================================

# ------------------------------------------------------------
# DONNEES HOPITAL DISTRICT KINKALA
# ------------------------------------------------------------
budget_kinkala = 12_500_000
consultations_kinkala = 1847
hospitalisations_kinkala = 201
deces_kinkala = 11
lits_total_kinkala = 45
lits_occupes_kinkala = 35
medecins_kinkala = 3
population_kinkala = 85_000

# ------------------------------------------------------------
# DONNEES CMS DE VINDZA
# ------------------------------------------------------------
budget_vindza = 6_800_000
consultations_vindza = 923
hospitalisations_vindza = 87
deces_vindza = 8
lits_total_vindza = 20
lits_occupes_vindza = 14
medecins_vindza = 1
population_vindza = 42_000

# ------------------------------------------------------------
# DONNEES HOPITAL DE KINDAMBA
# ------------------------------------------------------------
budget_kindamba = 9_200_000
consultations_kindamba = 1234
hospitalisations_kindamba = 312
deces_kindamba = 2
lits_total_kindamba = 41
lits_occupes_kindamba = 33
medecins_kindamba = 2
population_kindamba = 67_000

# ============================================================
# CALCULS KINKALA
# ============================================================

patients_kinkala = consultations_kinkala + hospitalisations_kinkala

cout_moyen_kinkala = round(
    budget_kinkala / patients_kinkala, 2
)

occupation_kinkala = round(
    (lits_occupes_kinkala / lits_total_kinkala) * 100, 2
)

densite_kinkala = round(
    (medecins_kinkala / population_kinkala) * 1000, 2
)

mortalite_kinkala = round(
    (deces_kinkala / hospitalisations_kinkala) * 100, 2
)

# ============================================================
# CALCULS VINDZA
# ============================================================

patients_vindza = consultations_vindza + hospitalisations_vindza

cout_moyen_vindza = round(
    budget_vindza / patients_vindza, 2
)

occupation_vindza = round(
    (lits_occupes_vindza / lits_total_vindza) * 100, 2
)

densite_vindza = round(
    (medecins_vindza / population_vindza) * 1000, 2
)

mortalite_vindza = round(
    (deces_vindza / hospitalisations_vindza) * 100, 2
)

# ============================================================
# CALCULS KINDAMBA
# ============================================================

patients_kindamba = consultations_kindamba + hospitalisations_kindamba

cout_moyen_kindamba = round(
    budget_kindamba / patients_kindamba, 2
)

occupation_kindamba = round(
    (lits_occupes_kindamba / lits_total_kindamba) * 100, 2
)

densite_kindamba = round(
    (medecins_kindamba / population_kindamba) * 1000, 2
)

mortalite_kindamba = round(
    (deces_kindamba / hospitalisations_kindamba) * 100, 2
)

# ============================================================
# IDENTIFICATION DES HOPITAUX CRITIQUES
# ============================================================

print("=" * 70)
print("RAPPORT COMPARATIF DES HOPITAUX DU POOL")
print("=" * 70)

print("\nHOPITAL DISTRICT KINKALA")
print(f"  Cout moyen/patient : {cout_moyen_kinkala:.2f} FCFA")
print(f"  Taux occupation    : {occupation_kinkala:.2f}%")
print(f"  Densite medicale   : {densite_kinkala:.2f} med./1000 hab")
print(f"  Taux mortalite     : {mortalite_kinkala:.2f}%")

if mortalite_kinkala > 2 or densite_kinkala < 0.05:
    print("  ALERTE : ETABLISSEMENT CRITIQUE")

print("\nCMS DE VINDZA")
print(f"  Cout moyen/patient : {cout_moyen_vindza:.2f} FCFA")
print(f"  Taux occupation    : {occupation_vindza:.2f}%")
print(f"  Densite medicale   : {densite_vindza:.2f} med./1000 hab")
print(f"  Taux mortalite     : {mortalite_vindza:.2f}%")

if mortalite_vindza > 2 or densite_vindza < 0.05:
    print("  ALERTE : ETABLISSEMENT CRITIQUE")

print("\nHOPITAL DE KINDAMBA")
print(f"  Cout moyen/patient : {cout_moyen_kindamba:.2f} FCFA")
print(f"  Taux occupation    : {occupation_kindamba:.2f}%")
print(f"  Densite medicale   : {densite_kindamba:.2f} med./1000 hab")
print(f"  Taux mortalite     : {mortalite_kindamba:.2f}%")

if mortalite_kindamba > 2 or densite_kindamba < 0.05:
    print("  ALERTE : ETABLISSEMENT CRITIQUE")

# ============================================================
# BONUS : 5 MEDECINS PAR HOPITAL
# ============================================================

budget_total = (
    budget_kinkala
    + budget_vindza
    + budget_kindamba
)

medecins_actuels = (
    medecins_kinkala
    + medecins_vindza
    + medecins_kindamba
)

medecins_cibles = 5 * 3
medecins_a_recruter = medecins_cibles - medecins_actuels

cout_recrutement = medecins_a_recruter * 1_200_000

print("\n" + "=" * 70)
print("ANALYSE BUDGETAIRE")
print("=" * 70)

print(f"Budget total disponible : {budget_total:,} FCFA".replace(",", " "))
print(f"Medecins actuels        : {medecins_actuels}")
print(f"Medecins cibles         : {medecins_cibles}")
print(f"A recruter              : {medecins_a_recruter}")
print(f"Cout recrutement        : {cout_recrutement:,} FCFA".replace(",", " "))

if budget_total >= cout_recrutement:
    print("RESULTAT : Budget suffisant pour atteindre 5 medecins par hopital.")
else:
    print("RESULTAT : Budget insuffisant pour atteindre 5 medecins par hopital.")

print("=" * 70)