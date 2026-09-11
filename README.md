# MPLURE — portfolio di Matteo Palumbo

Pagina di presentazione inviata nelle email a freddo. Italiano in home, inglese sotto `/en`.

## Come si aggiorna

Tutto nasce da `build_site.py`: struttura, CSS, script e i testi IT/EN (dizionari `IT` e `EN`).
Non modificare `index.html` a mano: verrebbe sovrascritto.

```bash
python3 build_site.py     # rigenera index.html e en/index.html
./deploy.sh               # commit + push + GitHub Pages (1-2 minuti)
```

Anteprima locale: `python3 -m http.server 8765` in questa cartella, poi http://localhost:8765/.

## Regole di contenuto (11 settembre 2026)

- Nessun nome di maison o di prodotto altrui: le campagne concept sono etichettate per categoria
  ("Couture · studio di concept") e i file si chiamano `c1-riviera`, `c2-concrete`, `c3-veil`.
- Nessun prezzo in pagina: i formati di lavoro restano, le cifre stanno nel preventivo.
- Nessun nome di testata nella presentazione.
- Le prove del metodo (`img/proof/`) partono da packshot pubblici di marchi italiani: categoria in
  didascalia, mai il nome del marchio come credito.
- Prima di ogni invio del link: tutti gli asset devono rispondere 200 sul live, IT ed EN
  (vedi `~/mplure-studio/sales` SKILL §8).

## Asset

- `img/c*-…` immagini delle tre campagne concept (≤ 1800 px, JPEG q84)
- `img/proof/*.jpg` composite reference | key visual (1800 px)
- `img/og.jpg` anteprima social 1200×630
- `media/*.mp4` film + `media/*-poster.jpg` poster
- `proof/` originali delle prove, usati anche per i DM Instagram
