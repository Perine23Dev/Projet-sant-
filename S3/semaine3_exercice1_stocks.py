# ============================================================
# AKIENI ACADEMY — Projet Santé Publique
# Semaine 3 — Exercice 1 : Classification Stocks Médicaments
# ============================================================

# -----------------------------
# DONNEES MEDICAMENTS
# -----------------------------

m1_nom = "Artemether-Lumefantrine"
m1_stock = 3200
m1_seuil_rupture = 2000
m1_cout_unitaire = 3500.0

m2_nom = "Amoxicilline 500mg"
m2_stock = 950
m2_seuil_rupture = 800
m2_cout_unitaire = 850.0

m3_nom = "Paracetamol 500mg"
m3_stock = 12400
m3_seuil_rupture = 3000
m3_cout_unitaire = 120.0

m4_nom = "SRO (sachets)"
m4_stock = 4200
m4_seuil_rupture = 5000
m4_cout_unitaire = 125.0

m5_nom = "Vaccin DTP-HepB-Hib"
m5_stock = 820
m5_seuil_rupture = 1000
m5_cout_unitaire = 8500.0

# ============================================================
# CLASSIFICATION M1
# ============================================================

if m1_stock <= m1_seuil_rupture:
    m1_statut = "RUPTURE CRITIQUE"
    m1_couleur = "[ROUGE]"
    m1_action = "Alerte immediate PNA — commande express sous 24h"

elif m1_stock <= m1_seuil_rupture * 1.5:
    m1_statut = "ALERTE STOCK"
    m1_couleur = "[ORANGE]"
    m1_action = "Commande urgente a declencher sous 72h"

elif m1_stock <= m1_seuil_rupture * 2:
    m1_statut = "STOCK LIMITE"
    m1_couleur = "[JAUNE]"
    m1_action = "Surveillance renforcee — planifier commande"

else:
    m1_statut = "STOCK NORMAL"
    m1_couleur = "[VERT]"
    m1_action = "Situation normale — suivi standard"

# ============================================================
# CLASSIFICATION M2
# ============================================================

if m2_stock <= m2_seuil_rupture:
    m2_statut = "RUPTURE CRITIQUE"
    m2_couleur = "[ROUGE]"
    m2_action = "Alerte immediate PNA — commande express sous 24h"

elif m2_stock <= m2_seuil_rupture * 1.5:
    m2_statut = "ALERTE STOCK"
    m2_couleur = "[ORANGE]"
    m2_action = "Commande urgente a declencher sous 72h"

elif m2_stock <= m2_seuil_rupture * 2:
    m2_statut = "STOCK LIMITE"
    m2_couleur = "[JAUNE]"
    m2_action = "Surveillance renforcee — planifier commande"

else:
    m2_statut = "STOCK NORMAL"
    m2_couleur = "[VERT]"
    m2_action = "Situation normale — suivi standard"

# ============================================================
# CLASSIFICATION M3
# ============================================================

if m3_stock <= m3_seuil_rupture:
    m3_statut = "RUPTURE CRITIQUE"
    m3_couleur = "[ROUGE]"
    m3_action = "Alerte immediate PNA — commande express sous 24h"

elif m3_stock <= m3_seuil_rupture * 1.5:
    m3_statut = "ALERTE STOCK"
    m3_couleur = "[ORANGE]"
    m3_action = "Commande urgente a declencher sous 72h"

elif m3_stock <= m3_seuil_rupture * 2:
    m3_statut = "STOCK LIMITE"
    m3_couleur = "[JAUNE]"
    m3_action = "Surveillance renforcee — planifier commande"

else:
    m3_statut = "STOCK NORMAL"
    m3_couleur = "[VERT]"
    m3_action = "Situation normale — suivi standard"

# ============================================================
# CLASSIFICATION M4
# ============================================================

if m4_stock <= m4_seuil_rupture:
    m4_statut = "RUPTURE CRITIQUE"
    m4_couleur = "[ROUGE]"
    m4_action = "Alerte immediate PNA — commande express sous 24h"

elif m4_stock <= m4_seuil_rupture * 1.5:
    m4_statut = "ALERTE STOCK"
    m4_couleur = "[ORANGE]"
    m4_action = "Commande urgente a declencher sous 72h"

elif m4_stock <= m4_seuil_rupture * 2:
    m4_statut = "STOCK LIMITE"
    m4_couleur = "[JAUNE]"
    m4_action = "Surveillance renforcee — planifier commande"

else:
    m4_statut = "STOCK NORMAL"
    m4_couleur = "[VERT]"
    m4_action = "Situation normale — suivi standard"

# ============================================================
# CLASSIFICATION M5
# ============================================================

if m5_stock <= m5_seuil_rupture:
    m5_statut = "RUPTURE CRITIQUE"
    m5_couleur = "[ROUGE]"
    m5_action = "Alerte immediate PNA — commande express sous 24h"

elif m5_stock <= m5_seuil_rupture * 1.5:
    m5_statut = "ALERTE STOCK"
    m5_couleur = "[ORANGE]"
    m5_action = "Commande urgente a declencher sous 72h"

elif m5_stock <= m5_seuil_rupture * 2:
    m5_statut = "STOCK LIMITE"
    m5_couleur = "[JAUNE]"
    m5_action = "Surveillance renforcee — planifier commande"

else:
    m5_statut = "STOCK NORMAL"
    m5_couleur = "[VERT]"
    m5_action = "Situation normale — suivi standard"

# ============================================================
# COMPTEURS
# ============================================================

nb_ruptures_critiques = 0
nb_alertes_stock = 0
nb_stocks_normaux = 0

if m1_statut == "RUPTURE CRITIQUE":
    nb_ruptures_critiques += 1
elif m1_statut == "ALERTE STOCK":
    nb_alertes_stock += 1
elif m1_statut == "STOCK NORMAL":
    nb_stocks_normaux += 1

if m2_statut == "RUPTURE CRITIQUE":
    nb_ruptures_critiques += 1
elif m2_statut == "ALERTE STOCK":
    nb_alertes_stock += 1
elif m2_statut == "STOCK NORMAL":
    nb_stocks_normaux += 1

if m3_statut == "RUPTURE CRITIQUE":
    nb_ruptures_critiques += 1
elif m3_statut == "ALERTE STOCK":
    nb_alertes_stock += 1
elif m3_statut == "STOCK NORMAL":
    nb_stocks_normaux += 1

if m4_statut == "RUPTURE CRITIQUE":
    nb_ruptures_critiques += 1
elif m4_statut == "ALERTE STOCK":
    nb_alertes_stock += 1
elif m4_statut == "STOCK NORMAL":
    nb_stocks_normaux += 1

if m5_statut == "RUPTURE CRITIQUE":
    nb_ruptures_critiques += 1
elif m5_statut == "ALERTE STOCK":
    nb_alertes_stock += 1
elif m5_statut == "STOCK NORMAL":
    nb_stocks_normaux += 1

# ============================================================
# RAPPORT
# ============================================================

print("=" * 65)
print(" RAPPORT DE STOCK — PHARMACIE NATIONALE D APPROVISIONNEMENT")
print(" Date : 15 janvier 2026")
print("=" * 65)

print(f"{m1_couleur} {m1_nom}")
print(f"Stock : {m1_stock} unites | Seuil rupture : {m1_seuil_rupture}")
print(f"Statut : {m1_statut}")
print(f"Action : {m1_action}")
print("-" * 65)

print(f"{m2_couleur} {m2_nom}")
print(f"Stock : {m2_stock} unites | Seuil rupture : {m2_seuil_rupture}")
print(f"Statut : {m2_statut}")
print(f"Action : {m2_action}")
print("-" * 65)

print(f"{m3_couleur} {m3_nom}")
print(f"Stock : {m3_stock} unites | Seuil rupture : {m3_seuil_rupture}")
print(f"Statut : {m3_statut}")
print(f"Action : {m3_action}")
print("-" * 65)

print(f"{m4_couleur} {m4_nom}")
print(f"Stock : {m4_stock} unites | Seuil rupture : {m4_seuil_rupture}")
print(f"Statut : {m4_statut}")
print(f"Action : {m4_action}")
print("-" * 65)

print(f"{m5_couleur} {m5_nom}")
print(f"Stock : {m5_stock} unites | Seuil rupture : {m5_seuil_rupture}")
print(f"Statut : {m5_statut}")
print(f"Action : {m5_action}")

print("=" * 65)
print("BILAN STOCK — PNA CONGO")
print(f"Ruptures critiques : {nb_ruptures_critiques}")
print(f"Alertes stock      : {nb_alertes_stock}")
print(f"Stocks normaux     : {nb_stocks_normaux}")
print("=" * 65)

if nb_ruptures_critiques > 0:
    print(f"!! ALERTE PRIORITAIRE : {nb_ruptures_critiques} medicaments en RUPTURE CRITIQUE !!")
    print("Transmettre immediatement au Dr. MOUKALA (PNA)")
else:
    print("Aucune rupture critique detectee.")

print("=" * 65)