# ============================================================
# AKIENI ACADEMY — Projet Sante Publique
# Semaine 2 — Exercice 2 : KPIs Sanitaires OMS
# ============================================================

# --- DONNEES BRUTES ---
budget_fcfa          = 87_450_000
nb_consultations_ext = 4823
nb_hospitalisations  = 1247
nb_deces             = 18
nb_lits_total        = 180
nb_lits_occupes      = 143
nb_medecins          = 22
nb_infirmiers        = 58
population_dept      = 128_000
taux_eur_fcfa        = 655.957
taux_usd_fcfa        = 600.0

# ============================================================
# 1. CONVERSIONS DEVISES
# ============================================================

budget_eur = round(budget_fcfa / taux_eur_fcfa, 2)
budget_usd = round(budget_fcfa / taux_usd_fcfa, 2)

# ============================================================
# 2. INDICATEURS OMS
# ============================================================

densite_medicale = round((nb_medecins / population_dept) * 1000, 1)
taux_mortalite = round((nb_deces / nb_hospitalisations) * 100, 1)
taux_occupation = round((nb_lits_occupes / nb_lits_total) * 100, 1)

# ============================================================
# 3. DIVISION ENTIERE ET MODULO
# ============================================================

budget_medicaments = int(budget_fcfa * 0.35)
cout_journalier_meds = 450_000

jours_stock = budget_medicaments // cout_journalier_meds
jours_restants = budget_medicaments % cout_journalier_meds

# ============================================================
# 4. PUISSANCE POUR PROJECTION
# ============================================================

budget_n_plus_2 = budget_fcfa * (1.08 ** 2)

# ============================================================
# 5. PAIR OU IMPAIR
# ============================================================

if nb_consultations_ext % 2 == 0:
    parite = "PAIR"
else:
    parite = "IMPAIR"

# ============================================================
# 6. AFFICHAGE DU RAPPORT
# ============================================================

print("=== RAPPORT TRIMESTRIEL Q4 2025 - Hopital General Pointe-Noire ===")

print("\nBUDGET")
print(f"  Depenses Q4       : {budget_fcfa:,} FCFA".replace(",", " "))
print(f"  En euros          : {budget_eur:.2f} EUR")
print(f"  En dollars        : {budget_usd:.2f} USD")

print("\nINDICATEURS OMS")
print(f"  Densite medicale  : {densite_medicale} medecins / 1000 hab  [Norme OMS : >= 2.3]")
print(f"  Taux mortalite    : {taux_mortalite}%                      [Seuil alerte : > 2%]")
print(f"  Taux occupation   : {taux_occupation}%                     [Optimal : 70-85%]")

print("\nANALYSE PHARMACIE")
print(f"  Budget medicaments: {budget_medicaments:,} FCFA".replace(",", " "))
print(f"  Jours de stock    : {jours_stock} jours")
print(f"  Jours depassement : {jours_restants} FCFA")

print("\nPROJECTION")
print(f"  Budget N+2 (8%/an): {budget_n_plus_2:.1f} FCFA")

print(f"\nConsultations externes : {nb_consultations_ext} ({parite})")

if densite_medicale < 2.3:
    print(
        f"\nALERTE : Densite medicale CRITIQUE "
        f"({densite_medicale} pour 1000 hab — norme OMS : 2.3)"
    )