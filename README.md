# Oraș plutitor SF – scenă 3D în Python

Acest proiect reprezintă o mini-scenă 3D de tip **oraș plutitor SF**, realizată în Python folosind biblioteca **VPython**. Scena conține o insulă plutitoare, turnuri, un nucleu energetic central, un inel energetic rotativ și o dronă care orbitează orașul.

## Tehnologii utilizate

- **Python 3** (//pentru logica programului.
- **VPython** (randare 3D interactivă, bazată pe WebGL în browser)

##  Elemente ale scenei: 

- **Insulă plutitoare: un „box” verde și un „cone” maro dedesubt (stânca). **
- **Nucleu energetic: un „sphere” emisiv, cu rază care pulsează în timp.**
- **Inel energetic: un „ring” care se rotește continuu în jurul nucleului.**
- **Turnuri: „cylinder” + „cone” dispuse circular în jurul nucleului.**
- **Platforme: „box” suplimentare pentru detalii vizuale. **
- **Dronă: un „box” + „cone” care orbitează insula și își orientează axa spre centru.**
- **Lumini locale: „local_light” pentru efect de iluminare SF.**
## Animație:
- **Folosim un loop „while True” cu „rate(60)” pentru ~60 FPS.**
- **Actualizăm pozițiile (plutirea insulei, orbita dronei) și rotațiile (inelul energetic) în funcție de timpul „t”.**

Instalare VPython:

```bash
pip install vpython
