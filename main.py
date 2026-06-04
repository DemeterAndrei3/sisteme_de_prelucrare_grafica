from vpython import *
import math

# ------------------------------
# Setări scenă
# ------------------------------
scene.title = "Oras plutitor SF - VPython"
scene.width = 1000
scene.height = 700
scene.background = color.black
scene.center = vector(0, 3, 0)

# ------------------------------
# Insula plutitoare (platforma)
# ------------------------------
insula = box(
    pos=vector(0, 0, 0),
    size=vector(20, 1, 20),
    color=vector(0.1, 0.6, 0.1),
    shininess=0.6
)

# Stânca de sub insulă
stanca = cone(
    pos=vector(0, -0.5, 0),
    axis=vector(0, -8, 0),
    radius=7,
    color=vector(0.4, 0.25, 0.1)
)

# ------------------------------
# Nucleu energetic central
# ------------------------------
nucleu = sphere(
    pos=vector(0, 2, 0),
    radius=1.2,
    color=color.cyan,
    emissive=True,
    shininess=1
)

# Inel energetic în jurul nucleului
inel = ring(
    pos=nucleu.pos,
    axis=vector(0, 1, 0),
    radius=4,
    thickness=0.2,
    color=color.white
)

# ------------------------------
# Turnuri în jurul nucleului
# ------------------------------
turnuri = []
numar_turnuri = 8
raza_turnuri = 7

for i in range(numar_turnuri):
    unghi = 2 * math.pi * i / numar_turnuri
    x = raza_turnuri * math.cos(unghi)
    z = raza_turnuri * math.sin(unghi)

    baza = cylinder(
        pos=vector(x, 0.5, z),
        axis=vector(0, 3, 0),
        radius=0.6,
        color=vector(0.5, 0.5, 0.8)
    )

    varf = cone(
        pos=baza.pos + vector(0, 3, 0),
        axis=vector(0, 1.5, 0),
        radius=1.0,
        color=vector(0.8, 0.8, 1.0)
    )

    turnuri.append((baza, varf))

# ------------------------------
# Platforme suplimentare (detalii)
# ------------------------------
platforme = []
for i in range(4):
    unghi = 2 * math.pi * i / 4
    x = 10 * math.cos(unghi)
    z = 10 * math.sin(unghi)
    p = box(
        pos=vector(x, 1.2, z),
        size=vector(4, 0.3, 4),
        color=vector(0.2, 0.2, 0.5)
    )
    platforme.append(p)

# ------------------------------
# Dronă care orbitează orașul
# ------------------------------
drone_body = box(
    pos=vector(12, 4, 0),
    size=vector(1.5, 0.5, 1),
    color=color.red
)

drone_nose = cone(
    pos=drone_body.pos + vector(0.9, 0, 0),
    axis=vector(0.8, 0, 0),
    radius=0.4,
    color=color.yellow
)

# Grupare logică: poziția de referință a dronei
drone_center = vector(12, 4, 0)

# ------------------------------
# Lumini
# ------------------------------
lumina_centrala = local_light(
    pos=vector(0, 5, 0),
    color=vector(0.4, 0.8, 1.0)
)

lumina_nucleu = local_light(
    pos=nucleu.pos,
    color=vector(0.2, 0.9, 0.9)
)

# ------------------------------
# Animație
# ------------------------------
t = 0
viteza_inel = 1.5      # viteza de rotatie a inelului
viteza_drona = 0.5     # viteza de rotatie a dronei
amplitudine_plutire = 0.5
viteza_plutire = 1.0

while True:
    rate(60)
    t += 0.02

    # Plutirea insulei (sus-jos)
    deplasare_y = amplitudine_plutire * math.sin(viteza_plutire * t)
    insula.pos.y = deplasare_y
    stanca.pos.y = deplasare_y - 0.5
    nucleu.pos.y = 2 + deplasare_y
    inel.pos = nucleu.pos

    # Ajustăm și turnurile și platformele
    for (baza, varf) in turnuri:
        baza.pos.y = 0.5 + deplasare_y
        varf.pos = baza.pos + vector(0, 3, 0)

    for p in platforme:
        p.pos.y = 1.2 + deplasare_y

    # Rotirea inelului energetic
    inel.rotate(
        angle=viteza_inel * 0.02,
        axis=vector(0, 1, 0),
        origin=nucleu.pos
    )

    # Pulsarea nucleului (schimbare ușoară de rază)
    nucleu.radius = 1.2 + 0.1 * math.sin(3 * t)

    # Drona orbitează în jurul insulei
    unghi_drona = viteza_drona * t
    raza_drona = 12
    drone_center = vector(
        raza_drona * math.cos(unghi_drona),
        4 + 0.3 * math.sin(2 * t),
        raza_drona * math.sin(unghi_drona)
    )

    drone_body.pos = drone_center
    drone_nose.pos = drone_body.pos + vector(0.9, 0, 0)

    # Orientăm drona spre centrul insulei
    directie = norm(vector(0, 2, 0) - drone_body.pos)
    drone_body.axis = directie
    drone_nose.axis = directie * 0.8
