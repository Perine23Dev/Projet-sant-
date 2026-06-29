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


# ============================================================
# SECTION F : CLASSIFICATION DES STOCKS
# ============================================================

# Médicament 1
if med1_qte <= med1_seuil:
    med1_statut = "RUPTURE CRITIQUE"
    med1_couleur = "[ROUGE]"
elif med1_qte <= med1_seuil * 1.5:
    med1_statut = "ALERTE STOCK"
    med1_couleur = "[ORANGE]"
elif med1_qte <= med1_seuil * 2:
    med1_statut = "STOCK LIMITE"
    med1_couleur = "[JAUNE]"
else:
    med1_statut = "STOCK NORMAL"
    med1_couleur = "[VERT]"

# Médicament 2
if med2_qte <= med2_seuil:
    med2_statut = "RUPTURE CRITIQUE"
    med2_couleur = "[ROUGE]"
elif med2_qte <= med2_seuil * 1.5:
    med2_statut = "ALERTE STOCK"
    med2_couleur = "[ORANGE]"
elif med2_qte <= med2_seuil * 2:
    med2_statut = "STOCK LIMITE"
    med2_couleur = "[JAUNE]"
else:
    med2_statut = "STOCK NORMAL"
    med2_couleur = "[VERT]"

# Médicament 3
if med3_qte <= med3_seuil:
    med3_statut = "RUPTURE CRITIQUE"
    med3_couleur = "[ROUGE]"
elif med3_qte <= med3_seuil * 1.5:
    med3_statut = "ALERTE STOCK"
    med3_couleur = "[ORANGE]"
elif med3_qte <= med3_seuil * 2:
    med3_statut = "STOCK LIMITE"
    med3_couleur = "[JAUNE]"
else:
    med3_statut = "STOCK NORMAL"
    med3_couleur = "[VERT]"

# Médicament 4
if med4_qte <= med4_seuil:
    med4_statut = "RUPTURE CRITIQUE"
    med4_couleur = "[ROUGE]"
elif med4_qte <= med4_seuil * 1.5:
    med4_statut = "ALERTE STOCK"
    med4_couleur = "[ORANGE]"
elif med4_qte <= med4_seuil * 2:
    med4_statut = "STOCK LIMITE"
    med4_couleur = "[JAUNE]"
else:
    med4_statut = "STOCK NORMAL"
    med4_couleur = "[VERT]"

# Médicament 5
if med5_qte <= med5_seuil:
    med5_statut = "RUPTURE CRITIQUE"
    med5_couleur = "[ROUGE]"
elif med5_qte <= med5_seuil * 1.5:
    med5_statut = "ALERTE STOCK"
    med5_couleur = "[ORANGE]"
elif med5_qte <= med5_seuil * 2:
    med5_statut = "STOCK LIMITE"
    med5_couleur = "[JAUNE]"
else:
    med5_statut = "STOCK NORMAL"
    med5_couleur = "[VERT]"

# ============================================================
# SECTION G : OCCUPATION DES HOPITAUX
# ============================================================

h1_taux = (h1_nb_lits_occupes / h1_nb_lits) * 100
h2_taux = (h2_nb_lits_occupes / h2_nb_lits) * 100
h3_taux = (h3_nb_lits_occupes / h3_nb_lits) * 100
h4_taux = (h4_nb_lits_occupes / h4_nb_lits) * 100
h5_taux = (h5_nb_lits_occupes / h5_nb_lits) * 100

# Hôpital 1
if h1_taux > 95:
    h1_niveau = "CRITIQUE"
elif h1_taux > 85:
    h1_niveau = "ELEVE"
elif h1_taux >= 60:
    h1_niveau = "OPTIMAL"
else:
    h1_niveau = "SOUS-UTILISE"

# Hôpital 2
if h2_taux > 95:
    h2_niveau = "CRITIQUE"
elif h2_taux > 85:
    h2_niveau = "ELEVE"
elif h2_taux >= 60:
    h2_niveau = "OPTIMAL"
else:
    h2_niveau = "SOUS-UTILISE"

# Hôpital 3
if h3_taux > 95:
    h3_niveau = "CRITIQUE"
elif h3_taux > 85:
    h3_niveau = "ELEVE"
elif h3_taux >= 60:
    h3_niveau = "OPTIMAL"
else:
    h3_niveau = "SOUS-UTILISE"

# Hôpital 4
if h4_taux > 95:
    h4_niveau = "CRITIQUE"
elif h4_taux > 85:
    h4_niveau = "ELEVE"
elif h4_taux >= 60:
    h4_niveau = "OPTIMAL"
else:
    h4_niveau = "SOUS-UTILISE"

# Hôpital 5
if h5_taux > 95:
    h5_niveau = "CRITIQUE"
elif h5_taux > 85:
    h5_niveau = "ELEVE"
elif h5_taux >= 60:
    h5_niveau = "OPTIMAL"
else:
    h5_niveau = "SOUS-UTILISE"

# ============================================================
# SECTION H : COUVERTURE VACCINALE
# ============================================================

brazzaville_population = 450000
brazzaville_vaccines = 418500

pointe_population = 280000
pointe_vaccines = 229600

pool_population = 120000
pool_vaccines = 54000

sangha_population = 85000
sangha_vaccines = 35700

brazzaville_taux = (brazzaville_vaccines / brazzaville_population) * 100
pointe_taux = (pointe_vaccines / pointe_population) * 100
pool_taux = (pool_vaccines / pool_population) * 100
sangha_taux = (sangha_vaccines / sangha_population) * 100

# Brazzaville
if brazzaville_taux < 50:
    brazzaville_statut = "ZONE CRITIQUE"
elif brazzaville_taux < 80:
    brazzaville_statut = "ZONE A RISQUE"
elif brazzaville_taux < SEUIL_OMS_COUVERTURE_VACCIN:
    brazzaville_statut = "ZONE INSUFFISANTE"
else:
    brazzaville_statut = "ZONE CONFORME"

# Pointe-Noire
if pointe_taux < 50:
    pointe_statut = "ZONE CRITIQUE"
elif pointe_taux < 80:
    pointe_statut = "ZONE A RISQUE"
elif pointe_taux < SEUIL_OMS_COUVERTURE_VACCIN:
    pointe_statut = "ZONE INSUFFISANTE"
else:
    pointe_statut = "ZONE CONFORME"

# Pool
if pool_taux < 50:
    pool_statut = "ZONE CRITIQUE"
elif pool_taux < 80:
    pool_statut = "ZONE A RISQUE"
elif pool_taux < SEUIL_OMS_COUVERTURE_VACCIN:
    pool_statut = "ZONE INSUFFISANTE"
else:
    pool_statut = "ZONE CONFORME"

# Sangha
if sangha_taux < 50:
    sangha_statut = "ZONE CRITIQUE"
elif sangha_taux < 80:
    sangha_statut = "ZONE A RISQUE"
elif sangha_taux < SEUIL_OMS_COUVERTURE_VACCIN:
    sangha_statut = "ZONE INSUFFISANTE"
else:
    sangha_statut = "ZONE CONFORME"

# ============================================================
# SECTION I : RAPPORT GLOBAL
# ============================================================

nb_ruptures = 0
nb_hopitaux_critiques = 0
nb_zones_critiques = 0

if med1_statut == "RUPTURE CRITIQUE":
    nb_ruptures += 1
if med2_statut == "RUPTURE CRITIQUE":
    nb_ruptures += 1
if med3_statut == "RUPTURE CRITIQUE":
    nb_ruptures += 1
if med4_statut == "RUPTURE CRITIQUE":
    nb_ruptures += 1
if med5_statut == "RUPTURE CRITIQUE":
    nb_ruptures += 1

if h1_niveau == "CRITIQUE":
    nb_hopitaux_critiques += 1
if h2_niveau == "CRITIQUE":
    nb_hopitaux_critiques += 1
if h3_niveau == "CRITIQUE":
    nb_hopitaux_critiques += 1
if h4_niveau == "CRITIQUE":
    nb_hopitaux_critiques += 1
if h5_niveau == "CRITIQUE":
    nb_hopitaux_critiques += 1

if brazzaville_statut == "ZONE CRITIQUE":
    nb_zones_critiques += 1
if pointe_statut == "ZONE CRITIQUE":
    nb_zones_critiques += 1
if pool_statut == "ZONE CRITIQUE":
    nb_zones_critiques += 1
if sangha_statut == "ZONE CRITIQUE":
    nb_zones_critiques += 1

print("\n" + "=" * 65)
print("RAPPORT D'ETAT GLOBAL")
print("=" * 65)

print("\nSTATUT DES MEDICAMENTS")
print(f"{med1_nom} : {med1_couleur} {med1_statut}")
print(f"{med2_nom} : {med2_couleur} {med2_statut}")
print(f"{med3_nom} : {med3_couleur} {med3_statut}")
print(f"{med4_nom} : {med4_couleur} {med4_statut}")
print(f"{med5_nom} : {med5_couleur} {med5_statut}")

print("\nOCCUPATION DES HOPITAUX")
print(f"{h1_nom} : {h1_taux:.1f}% - {h1_niveau}")
print(f"{h2_nom} : {h2_taux:.1f}% - {h2_niveau}")
print(f"{h3_nom} : {h3_taux:.1f}% - {h3_niveau}")
print(f"{h4_nom} : {h4_taux:.1f}% - {h4_niveau}")
print(f"{h5_nom} : {h5_taux:.1f}% - {h5_niveau}")

print("\nCOUVERTURE VACCINALE")
print(f"Brazzaville : {brazzaville_taux:.1f}% - {brazzaville_statut}")
print(f"Pointe-Noire : {pointe_taux:.1f}% - {pointe_statut}")
print(f"Pool : {pool_taux:.1f}% - {pool_statut}")
print(f"Sangha : {sangha_taux:.1f}% - {sangha_statut}")

print("\nRESUME EXECUTIF")
print(f"Ruptures critiques : {nb_ruptures}")
print(f"Hopitaux critiques : {nb_hopitaux_critiques}")
print(f"Zones vaccinales critiques : {nb_zones_critiques}")

print("=" * 65)