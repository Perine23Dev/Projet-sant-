# ============================================================
# MODULE FONDATEUR — Projet Santé Publique / Akieni Academy
# ============================================================

# ============================================================
# SECTION A : CONSTANTES NATIONALES ET NORMES OMS
# ============================================================

TAUX_EUR_FCFA = 655.957
TAUX_USD_FCFA = 600.0

SEUIL_OMS_DENSITE_MEDICALE = 2.3
SEUIL_OMS_COUVERTURE_VACCIN = 95.0
SEUIL_MORTALITE_ALERTE = 2.0
SEUIL_RUPTURE_STOCK_JOURS = 30

DEPARTEMENTS_CONGO = [
    "Brazzaville",
    "Pointe-Noire",
    "Bouenza",
    "Cuvette",
    "Cuvette-Ouest",
    "Kouilou",
    "Lekoumou",
    "Likouala",
    "Niari",
    "Plateaux",
    "Pool",
    "Sangha"
]

# ============================================================
# SECTION B : LES 5 HOPITAUX
# ============================================================

# H1
h1_nom = "CHU de Brazzaville"
h1_ville = "Brazzaville"
h1_departement = "Brazzaville"
h1_type = "CHU"
h1_nb_lits = 320
h1_nb_lits_occupes = 284
h1_nb_medecins = 47
h1_nb_infirmiers = 123
h1_population_zone = 1_800_000

# H2
h2_nom = "Hopital General Pointe-Noire"
h2_ville = "Pointe-Noire"
h2_departement = "Pointe-Noire"
h2_type = "Hopital General"
h2_nb_lits = 180
h2_nb_lits_occupes = 143
h2_nb_medecins = 22
h2_nb_infirmiers = 58
h2_population_zone = 900_000

# H3
h3_nom = "Hopital de Dolisie"
h3_ville = "Dolisie"
h3_departement = "Niari"
h3_type = "Hopital Regional"
h3_nb_lits = 120
h3_nb_lits_occupes = 87
h3_nb_medecins = 15
h3_nb_infirmiers = 41
h3_population_zone = 350_000

# H4
h4_nom = "Hopital de District Owando"
h4_ville = "Owando"
h4_departement = "Cuvette"
h4_type = "District"
h4_nb_lits = 80
h4_nb_lits_occupes = 54
h4_nb_medecins = 8
h4_nb_infirmiers = 22
h4_population_zone = 120_000

# H5
h5_nom = "Centre de Sante Impfondo"
h5_ville = "Impfondo"
h5_departement = "Likouala"
h5_type = "Centre de Sante"
h5_nb_lits = 50
h5_nb_lits_occupes = 31
h5_nb_medecins = 4
h5_nb_infirmiers = 12
h5_population_zone = 80_000

# ============================================================
# SECTION C : MEDICAMENTS ESSENTIELS
# ============================================================

med1_nom = "Artemether-Lumefantrine"
med1_qte = 5000
med1_seuil = 1000
med1_cout = 1500.0

med2_nom = "Amoxicilline"
med2_qte = 8000
med2_seuil = 1500
med2_cout = 500.0

med3_nom = "Paracetamol"
med3_qte = 12000
med3_seuil = 2000
med3_cout = 100.0

med4_nom = "SRO"
med4_qte = 4000
med4_seuil = 500
med4_cout = 300.0

med5_nom = "Vaccin Antipaludeen"
med5_qte = 2000
med5_seuil = 400
med5_cout = 5000.0

# ============================================================
# SECTION D : CALCULS D'INITIALISATION
# ============================================================

total_medecins = (
    h1_nb_medecins +
    h2_nb_medecins +
    h3_nb_medecins +
    h4_nb_medecins +
    h5_nb_medecins
)

population_totale = (
    h1_population_zone +
    h2_population_zone +
    h3_population_zone +
    h4_population_zone +
    h5_population_zone
)

densite_nationale = round(
    (total_medecins / population_totale) * 1000,
    2
)

total_lits = (
    h1_nb_lits +
    h2_nb_lits +
    h3_nb_lits +
    h4_nb_lits +
    h5_nb_lits
)

total_lits_occupes = (
    h1_nb_lits_occupes +
    h2_nb_lits_occupes +
    h3_nb_lits_occupes +
    h4_nb_lits_occupes +
    h5_nb_lits_occupes
)

taux_occupation_moyen = round(
    (total_lits_occupes / total_lits) * 100,
    2
)

valeur_stock = (
    med1_qte * med1_cout +
    med2_qte * med2_cout +
    med3_qte * med3_cout +
    med4_qte * med4_cout +
    med5_qte * med5_cout
)

# ============================================================
# SECTION E : RAPPORT D'INVENTAIRE
# ============================================================

print("=" * 60)
print("SYSTEME NATIONAL DE SANTE")
print("=" * 60)

print("\nHOPITAUX ENREGISTRES :", 5)
print("DEPARTEMENTS :", len(DEPARTEMENTS_CONGO))

print("\nKPIs NATIONAUX")
print(f"Densite medicale nationale : {densite_nationale}")
print(f"Taux occupation moyen      : {taux_occupation_moyen}%")
print(f"Valeur stock medicaments   : {valeur_stock:,.0f} FCFA".replace(",", " "))

print("\nMEDICAMENTS ESSENTIELS")
print(f"- {med1_nom}")
print(f"- {med2_nom}")
print(f"- {med3_nom}")
print(f"- {med4_nom}")
print(f"- {med5_nom}")

print("\nSTATUT INITIAL : SYSTEME CHARGE AVEC SUCCES")
print("=" * 60)