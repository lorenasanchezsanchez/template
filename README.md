# curs-git
![portada](docs/img/portada-cefire.png)

Repositori amb el material didàctic del curs de formació __Introducció a Git i la seua aplicació a l’aula__.

El material didàctic es pot consultar a [https://lorenasanchezsanchez.github.io/CURS_GIT/](https://lorenasanchezsanchez.github.io/CURS_GIT/).

## Publicació amb GitHub Pages

Este repositori està configurat per a publicar automàticament el lloc de MkDocs amb GitHub Pages:

- Cada vegada que es fa un push a la branca `main`, GitHub Actions construeix el lloc i el desplega.
- El flux de treball està en `.github/workflows/pages.yml`.
- La web queda disponible a: https://lorenasanchezsanchez.github.io/CURS_GIT/

Per a provar en local:

1. Instal·la les dependències amb Python: `pip install -r requirements.txt`.
2. Servix el lloc: `mkdocs serve`.
3. Obri el navegador en `http://127.0.0.1:8000` (o el port indicat al fitxer `mkdocs.yml`).
