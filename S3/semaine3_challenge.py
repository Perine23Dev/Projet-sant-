# ============================================================
# AKIENI ACADEMY — Projet Santé Publique
# Semaine 3 — Challenge : Tableau de Bord Sanitaire
# ============================================================

# ------------------------------------------------------------
# DONNEES DES 5 HOPITAUX
# ------------------------------------------------------------

# CHU Brazzaville
chu_nom = "CHU Brazzaville"
chu_lits_totaux = 320
chu_lits_occupes = 298
chu_nb_medecins = 47
chu_nb_ruptures = 2
chu_nb_alertes = 2

# Hopital Pointe-Noire
pn_nom = "Hopital Pointe-Noire"
pn_lits_totaux = 180
pn_lits_occupes = 143
pn_nb_medecins = 22
pn_nb_ruptures = 0
pn_nb_alertes = 1

# Hopital Dolisie
dol_nom = "Hopital Dolisie"
dol_lits_totaux = 95
dol_lits_occupes = 91
dol_nb_medecins = 8
dol_nb_ruptures = 1
dol_nb_alertes = 2

# Hopital Owando
owa_nom = "Hopital Owando"
owa_lits_totaux = 45
owa_lits_occupes = 32
owa_nb_medecins = 3
owa_nb_ruptures = 3
owa_nb_alertes = 0

# CMS Impfondo
imp_nom = "CMS Impfondo"
imp_lits_totaux = 20
imp_lits_occupes = 19
imp_nb_medecins = 1
imp_nb_ruptures = 2
imp_nb_alertes = 1

# ------------------------------------------------------------
# CALCUL DES TAUX D'OCCUPATION
# ------------------------------------------------------------

chu_taux = (chu_lits_occupes / chu_lits_totaux) * 100
pn_taux = (pn_lits_occupes / pn_lits_totaux) * 100
dol_taux = (dol_lits_occupes / dol_lits_totaux) * 100
owa_taux = (owa_lits_occupes / owa_lits_totaux) * 100
imp_taux = (imp_lits_occupes / imp_lits_totaux) * 100

# ------------------------------------------------------------
# NIVEAU OCCUPATION
# ------------------------------------------------------------

# CHU
if chu_taux > 95:
    chu_occ = "[CRI]"
elif chu_taux > 85:
    chu_occ = "[ALT]"
else:
    chu_occ = "[OK ]"

# Pointe-Noire
if pn_taux > 95:
    pn_occ = "[CRI]"
elif pn_taux > 85:
    pn_occ = "[ALT]"
else:
    pn_occ = "[OK ]"

# Dolisie
if dol_taux > 95:
    dol_occ = "[CRI]"
elif dol_taux > 85:
    dol_occ = "[ALT]"
else:
    dol_occ = "[OK ]"

# Owando
if owa_taux > 95:
    owa_occ = "[CRI]"
elif owa_taux > 85:
    owa_occ = "[ALT]"
else:
    owa_occ = "[OK ]"

# Impfondo
if imp_taux > 95:
    imp_occ = "[CRI]"
elif imp_taux > 85:
    imp_occ = "[ALT]"
else:
    imp_occ = "[OK ]"

# ------------------------------------------------------------
# NIVEAU D'ALERTE GLOBAL
# ------------------------------------------------------------

# CHU
if chu_nb_ruptures >= 2 or chu_taux > 95:
    chu_niveau = "CRITIQUE"
    chu_action = "Mobiliser immediatement la reserve PNA."
elif chu_nb_ruptures >= 1 or chu_taux > 85 or (chu_nb_alertes >= 2 and chu_nb_medecins < 5):
    chu_niveau = "PREOCCUPANT"
    chu_action = "Renforcer la surveillance."
else:
    chu_niveau = "SATISFAISANT"
    chu_action = "Suivi normal."

# Pointe-Noire
if pn_nb_ruptures >= 2 or pn_taux > 95:
    pn_niveau = "CRITIQUE"
    pn_action = "Mobiliser immediatement la reserve PNA."
elif pn_nb_ruptures >= 1 or pn_taux > 85 or (pn_nb_alertes >= 2 and pn_nb_medecins < 5):
    pn_niveau = "PREOCCUPANT"
    pn_action = "Renforcer la surveillance."
else:
    pn_niveau = "SATISFAISANT"
    pn_action = "Suivi normal."

# Dolisie
if dol_nb_ruptures >= 2 or dol_taux > 95:
    dol_niveau = "CRITIQUE"
    dol_action = "Mobiliser immediatement la reserve PNA."
elif dol_nb_ruptures >= 1 or dol_taux > 85 or (dol_nb_alertes >= 2 and dol_nb_medecins < 5):
    dol_niveau = "PREOCCUPANT"
    dol_action = "Renforcer la surveillance."
else:
    dol_niveau = "SATISFAISANT"
    dol_action = "Suivi normal."

# Owando
if owa_nb_ruptures >= 2 or owa_taux > 95:
    owa_niveau = "CRITIQUE"
    owa_action = "Mobiliser immediatement la reserve PNA."
elif owa_nb_ruptures >= 1 or owa_taux > 85 or (owa_nb_alertes >= 2 and owa_nb_medecins < 5):
    owa_niveau = "PREOCCUPANT"
    owa_action = "Renforcer la surveillance."
else:
    owa_niveau = "SATISFAISANT"
    owa_action = "Suivi normal."

# Impfondo
if imp_nb_ruptures >= 2 or imp_taux > 95:
    imp_niveau = "CRITIQUE"
    imp_action = "Mobiliser immediatement la reserve PNA."
elif imp_nb_ruptures >= 1 or imp_taux > 85 or (imp_nb_alertes >= 2 and imp_nb_medecins < 5):
    imp_niveau = "PREOCCUPANT"
    imp_action = "Renforcer la surveillance."
else:
    imp_niveau = "SATISFAISANT"
    imp_action = "Suivi normal."

# ------------------------------------------------------------
# COMPTEURS NATIONAUX
# ------------------------------------------------------------

nb_hopitaux_critiques = 0

if chu_niveau == "CRITIQUE":
    nb_hopitaux_critiques += 1

if pn_niveau == "CRITIQUE":
    nb_hopitaux_critiques += 1

if dol_niveau == "CRITIQUE":
    nb_hopitaux_critiques += 1

if owa_niveau == "CRITIQUE":
    nb_hopitaux_critiques += 1

if imp_niveau == "CRITIQUE":
    nb_hopitaux_critiques += 1

total_ruptures = (
    chu_nb_ruptures +
    pn_nb_ruptures +
    dol_nb_ruptures +
    owa_nb_ruptures +
    imp_nb_ruptures
)

cout_total = total_ruptures * 450000

# ------------------------------------------------------------
# TABLEAU DE BORD
# ------------------------------------------------------------

print("=" * 72)
print(" TABLEAU DE BORD SANITAIRE — MINISTERE DE LA SANTE")
print(" Date : 16 janvier 2026 | Pour le Conseil des Ministres")
print("=" * 72)

print(f"{'HOPITAL':28} {'OCCUPATION':15} {'ALERTES':12} NIVEAU GLOBAL")

print(f"{chu_nom:28} {chu_taux:5.1f}% {chu_occ:5}   {chu_nb_ruptures}R + {chu_nb_alertes}A     [{chu_niveau}]")
print(f"{pn_nom:28} {pn_taux:5.1f}% {pn_occ:5}   {pn_nb_ruptures}R + {pn_nb_alertes}A     [{pn_niveau}]")
print(f"{dol_nom:28} {dol_taux:5.1f}% {dol_occ:5}   {dol_nb_ruptures}R + {dol_nb_alertes}A     [{dol_niveau}]")
print(f"{owa_nom:28} {owa_taux:5.1f}% {owa_occ:5}   {owa_nb_ruptures}R + {owa_nb_alertes}A     [{owa_niveau}]")
print(f"{imp_nom:28} {imp_taux:5.1f}% {imp_occ:5}   {imp_nb_ruptures}R + {imp_nb_alertes}A     [{imp_niveau}]")

print("-" * 72)

print(f"{nb_hopitaux_critiques} hopitaux sur 5 en situation CRITIQUE")
print(f"{total_ruptures} ruptures de stock identifiees a l'echelle nationale")
print(f"Cout estime des commandes urgentes : {cout_total:,} FCFA")

print("RECOMMANDATION PRIORITAIRE : Mobiliser la reserve nationale PNA")

print("=" * 72)