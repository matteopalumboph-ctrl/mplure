#!/usr/bin/env python3
"""Genera index.html (IT) e en/index.html (EN) del portfolio MPLURE da un unico template.

    python3 build_site.py        # scrive i due file, poi ./deploy.sh

Una sola fonte per struttura, CSS e script: i testi vivono nei due dizionari IT / EN.
Le dimensioni delle immagini vengono lette dai file (width/height evitano i salti di layout).
Regole di contenuto (11 settembre 2026, dopo la revisione con tre lenti esterne):
- nessun nome di maison o di prodotto altrui: le campagne concept sono etichettate per categoria;
- nessun prezzo in pagina: i formati di lavoro restano, le cifre vanno nel preventivo;
- nessun nome di testata nella presentazione (regola di Matteo del 10/9);
- prima persona singolare ovunque: chi risponde è chi fa le immagini.
"""
import html
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent
BASE_URL = "https://matteopalumboph-ctrl.github.io/mplure/"
HERO = "img/c3-veil-campaign-campaign-01.jpg"


def dims(rel: str) -> str:
    w, h = Image.open(ROOT / rel).size
    return f'width="{w}" height="{h}"'


def esc(s: str) -> str:
    return html.escape(s, quote=False)


# --------------------------------------------------------------------------- contenuti
PROOFS = [  # slug, (it categoria, it descrizione), (en category, en description)
    ("sabadi", ("Cioccolato di Modica — Sicilia", "Packaging illustrato, testo compreso, dal packshot su fondo neutro a una lastra di pietra al sole."),
               ("Modica chocolate — Sicily", "Illustrated packaging, text included, from a neutral packshot to a stone slab in the sun.")),
    ("gobino", ("Cioccolateria — Torino", "La scatola aperta su un tavolo di marmo, un caffè, la luce di fine pomeriggio."),
               ("Chocolatier — Turin", "The open box on a marble table, an espresso, late-afternoon light.")),
    ("fssa", ("Profumeria storica — Firenze", "Il flacone su un baule di cuoio, la spezieria dietro, una foglia d'alloro."),
             ("Historic perfumery — Florence", "The bottle on a leather trunk, the apothecary cabinet behind, a bay leaf.")),
    ("faced", ("Skincare", "Il vasetto sul travertino, gocce d'acqua, luce laterale."),
              ("Skincare", "The jar on travertine, drops of water, side light.")),
    ("franceschetti", ("Calzatura artigianale — Marche", "La doppia fibbia sul gradino di pietra, il banco del calzolaio fuori fuoco."),
                      ("Handmade footwear — Marche", "The double monk on a stone step, the cobbler's bench out of focus.")),
    ("movitra", ("Occhialeria", "La montatura in acetato accanto a un libro aperto, luce da finestra."),
                ("Eyewear", "The acetate frame next to an open book, window light.")),
    ("biffoli", ("Gioielleria — Firenze", "Chevalier in argento brunito e oro, indossato, sul raso."),
                ("Jewellery — Florence", "Burnished silver and gold signet ring, worn, on satin.")),
    ("masara", ("Swimwear — Milano", "Il costume intero, dal packshot e-commerce al bordo piscina in cemento."),
               ("Swimwear — Milan", "The one-piece, from the e-commerce packshot to a concrete poolside.")),
]

WORKS = [
    dict(slug="c3-veil", title="Desert Veil", film="veil",
         imgs=["campaign-campaign-01", "campaign-campaign-03", "campaign-campaign-04", "hero-hero"],
         it=dict(meta="Couture · studio di concept · 2026",
                 body="Tele bianche tese sulla sabbia, mosse dal vento. Al centro una donna con la vitiligine, la pelle che riprende le ombre della stoffa. Sartoria nera su terra sbiancata, un ghepardo accanto, calmo; più in là un dromedario. Niente è decorativo: il deserto riduce l'immagine a pelle, tessuto e silenzio.",
                 cap="Diciannove secondi: stesso deserto, stessi teli, stesso abito delle fotografie."),
         en=dict(meta="Couture · concept study · 2026",
                 body="White canvas strung across the sand, moving in the wind. A woman with vitiligo at the centre, her skin echoing the shadows on the cloth. Black tailoring against bleached ground, a cheetah beside her, calm; further on, a camel. Nothing is decorative: the desert strips the image down to skin, cloth and silence.",
                 cap="Nineteen seconds: same desert, same canvases, same dress as the stills.")),
    dict(slug="c2-concrete", title="Concrete Ballroom", film="concrete",
         imgs=["hero-hero", "campaign-campaign-01", "campaign-campaign-02", "campaign-campaign-03"],
         it=dict(meta="Sportswear · studio di concept · 2026",
                 body="Una gonna da ballo costruita in jacquard tecnico, indossata contro il cemento grezzo a mezzogiorno. Le bande laterali corrono tra le pieghe come una vena d'oro. Postura sportiva, volume couture, nessun sorriso: la tensione tra lo stadio e il salone.",
                 cap="Dodici secondi verticali: stessa modella, stesso cemento, stesso capo delle fotografie."),
         en=dict(meta="Sportswear · concept study · 2026",
                 body="A ball skirt built from technical jacquard, worn against raw concrete at midday. The side stripes run through the pleats like a seam of gold. Sport posture, couture volume, no smile: the tension between the stadium and the salon.",
                 cap="Twelve vertical seconds: same model, same concrete, same garment as the stills.")),
    dict(slug="c1-riviera", title="Salt and Silk", film="riviera",
         imgs=["campaign-campaign-01", "campaign-campaign-02", "campaign-campaign-03", "hero-hero"],
         it=dict(meta="Resort e swimwear · studio di concept · 2026",
                 body="Una donna attraversa un solo giorno mediterraneo: la stanza con le persiane, il colonnato, il sentiero sulla scogliera, il mare aperto. La stampa è l'unico colore in un mondo di calce, pietra e acqua. Calore, sale, nessuno spettacolo: si deve sentire l'ora prima del tramonto, non un lancio di prodotto.",
                 cap="Undici secondi verticali, tre scene. Montato dallo stesso mondo delle immagini, nella stessa produzione."),
         en=dict(meta="Resort & swimwear · concept study · 2026",
                 body="A woman moves through a single Mediterranean day: shuttered room, colonnade, cliff path, open sea. The print is the only colour in a world of lime plaster, stone and water. Heat, salt, no spectacle: the viewer should feel the hour before sunset, not a product launch.",
                 cap="Eleven vertical seconds, three scenes. Edited from the same world as the stills, in the same production.")),
]

FILMS = [
    ("film-gown", "Abito da sera — fashion film", "Evening gown — fashion film"),
    ("film-jewels", "Alta gioielleria, in esterna", "Fine jewellery, on location"),
    ("film-beach", "Beachwear, costa lavica", "Beachwear, lava coast"),
    ("film-fragrance", "Fragranza, still life in movimento", "Fragrance, still life in motion"),
]

IT = dict(
    lang="it", other_lang="EN", prefix="", aria_sections="Sezioni",
    title="Matteo Palumbo — MPLURE · Campagne costruite intorno al vostro prodotto",
    description="Matteo Palumbo, fotografo di moda. Campagne pubblicitarie complete — concept, key visual, film — costruite intorno al vostro prodotto, senza organizzare uno shooting. Dirette da un fotografo, non da un prompt.",
    nav_work="Campagne", nav_method="Metodo", nav_contact="Contatti",
    eyebrow="Fotografo di moda · direzione creativa", h1="Matteo Palumbo",
    sub="Campagne complete — concept, key visual, film — costruite intorno al vostro prodotto. Dirette da un fotografo, non da un prompt.",
    hero_cta="Guarda le campagne", scroll="Scorri",
    lede="Vent'anni di editoriali e campagne mi hanno insegnato una cosa: il prodotto è già la campagna. Manca solo il mondo intorno. Oggi lo costruisco senza organizzare uno shooting, con la stessa direzione di sempre.",
    s_work="01 — Campagne", h_work="Tre mondi completi",
    p_work="Immagini e film nella stessa produzione. Sono studi di concept prodotti in autonomia, non commissionati e non collegati ad alcun marchio: mostrano fino a dove arriva il metodo quando il brief lo permette.",
    status="Studio di concept — non commissionato", film_lbl="Il film della campagna",
    mid_cta="Un test sul vostro prodotto",
    s_proof="02 — Dal packshot alla campagna", h_proof="Il prodotto è quello. Cambia il mondo intorno.",
    p_proof="Non serve uno shooting: serve la fotografia che avete già. Il packshot su fondo bianco dell'e-commerce contiene forma, colore, materiale, testi, finiture. Da lì costruisco il mondo intorno al prodotto, che resta identico a com'è. Otto prove, otto categorie — cioccolato, profumo, skincare, calzatura, occhiale, gioiello, swimwear — tutte da packshot pubblici di marchi italiani.",
    lbl_from="Reference del cliente", lbl_to="Key visual",
    proof_note="Prove realizzate in autonomia da immagini pubbliche, non commissionate dai marchi. Servono a mostrare il metodo, non un rapporto di lavoro.",
    s_motion="03 — Motion", h_motion="Ogni campagna si muove",
    p_motion="Il film non è un progetto separato con un budget separato: nasce dallo stesso mondo delle immagini, nella stessa produzione. Formati verticali per social e punto vendita. Anche questi sono studi di concept, non commissionati.",
    s_studio="04 — Lo studio", h_studio="Chi risponde è chi fa le immagini",
    studio=["Sono Matteo Palumbo, fotografo di moda: vent'anni tra editoriali e campagne per riviste e brand internazionali. MPLURE è il nome che do al mio lavoro di oggi.",
            "Una campagna ha sempre voluto dire una location, una troupe, un fitting e quattro-sei settimane. Per la maggior parte dei brand quel costo è il motivo per cui tre quarti dei prodotti non hanno mai una campagna vera.",
            "Produco lo stesso risultato — con art direction, coerente con il brand, nei formati pronti per paid, retail ed e-commerce — partendo dal prodotto che avete già. La tecnologia è il motore produttivo; quello che comprate è la campagna, con lo sguardo di chi le campagne le ha fatte per vent'anni."],
    facts=[("Esperienza", "Vent'anni di editoriali e campagne: moda, beauty, prodotto"),
           ("Struttura", "Lavoro da solo: nessun passaggio tra chi vende e chi produce"),
           ("Tempi", "Prima consegna in 5–7 giorni, due round di revisione inclusi"),
           ("Consegna", "File master ad alta risoluzione per stampa e affissione, versioni per web e social")],
    s_how="05 — Come funziona", h_how="Quattro passaggi",
    steps=[("01 Reference", "Mi mandate il prodotto, le reference e le eventuali linee guida di brand. Una call di trenta minuti."),
           ("02 Concept", "Concept creativo, art direction e mondo visivo, approvati prima che la produzione inizi."),
           ("03 Produzione", "Visual e film prodotti, gradati e ritoccati in un'unica lavorazione controllata."),
           ("04 Consegna", "Prima consegna in 5–7 giorni. Due round di revisione. File master e versioni ottimizzate per il web.")],
    s_eng="06 — Formati di lavoro", h_eng="Come lavoro con voi",
    offers=[("Still life di campagna", "Tre key visual su un prodotto, tre concept, formati advertising e social, post-produzione, un round di revisione. Il punto d'ingresso per un lancio o una scheda prodotto."),
            ("Campagna", "Concept creativo, art direction, sei key visual, due ambientazioni narrative, formati social, un film breve, color grading, due round di revisione."),
            ("Stagione", "Identità di campagna, dieci-quindici visual, tre-cinque scene narrative, tre film, adattamenti social ed e-commerce, hero image, storyboard, file master."),
            ("Partnership", "Produzione continuativa: sei-otto visual e due film al mese, adattamenti social, concept di campagna, priorità di consegna.")],
    eng_note="Il preventivo dipende da formati, mercati e diritti d'uso: arriva scritto entro 24 ore dalla call. Ogni progetto parte da un concept approvato, nessuna produzione alla cieca.",
    s_why="07 — Cosa garantisco",
    why=[("Fedeltà del prodotto", "Forma, logo, colore, testi e finiture riprodotti dalla vostra reference e verificati uno per uno contro l'originale. Dove il testo deve essere perfetto, il pack viene rimontato dal file originale in post-produzione."),
         ("Diritti d'uso", "Gli output consegnati sono vostri, per tutti i canali e senza limiti di tempo, salvo esclusive concordate nel preventivo."),
         ("Persone e trasparenza", "Nessuna persona reale riprodotta senza liberatoria. Dove la normativa lo richiede, l'origine generativa delle immagini viene dichiarata."),
         ("Controllo", "Concept approvato prima della produzione, un solo interlocutore dal concept ai file master, due round di revisione inclusi.")],
    h_contact="Parliamo del vostro prodotto.",
    p_contact="Mandatemi un packshot e un'idea di dove vorreste vederlo. Rispondo io, entro un giorno lavorativo, con una proposta di prova.",
    cta="Scrivimi", cta_wa="WhatsApp", avail="Aperto a nuovi brief: stagione SS27",
    role="Fotografo · direzione creativa",
    legal="Le campagne e i film mostrati sono studi di concept prodotti in autonomia, non commissionati e non collegati ad alcun marchio. Le prove del metodo partono da immagini pubbliche dei prodotti citati.",
)

EN = dict(
    lang="en", other_lang="IT", prefix="../", aria_sections="Sections",
    title="Matteo Palumbo — MPLURE · Campaigns built around your product",
    description="Matteo Palumbo, fashion photographer. Complete advertising campaigns — concept, key visuals, film — built around your product, without organising a shoot. Directed by a photographer, not by a prompt.",
    nav_work="Campaigns", nav_method="Method", nav_contact="Contact",
    eyebrow="Fashion photographer · creative direction", h1="Matteo Palumbo",
    sub="Complete campaigns — concept, key visuals, film — built around your product. Directed by a photographer, not by a prompt.",
    hero_cta="See the campaigns", scroll="Scroll",
    lede="Twenty years of editorials and campaigns taught me one thing: the product already is the campaign. Only the world around it is missing. Today I build it without organising a shoot, with the same direction as always.",
    s_work="01 — Campaigns", h_work="Three complete worlds",
    p_work="Stills and film in the same production. These are concept studies, self-produced, not commissioned and unaffiliated with any brand: they show how far the method goes when the brief allows it.",
    status="Concept study — not commissioned", film_lbl="The campaign film",
    mid_cta="A test on your product",
    s_proof="02 — From packshot to campaign", h_proof="The product stays the same. The world around it changes.",
    p_proof="No shoot needed: the photograph you already have is enough. The white-background e-commerce packshot holds shape, colour, material, text, finish. From there I build the world around the product, which stays exactly as it is. Eight proofs, eight categories — chocolate, fragrance, skincare, footwear, eyewear, jewellery, swimwear — all from public packshots of Italian brands.",
    lbl_from="Client reference", lbl_to="Key visual",
    proof_note="Proofs made independently from public images, not commissioned by the brands. They show the method, not a working relationship.",
    s_motion="03 — Motion", h_motion="Every campaign moves",
    p_motion="The film is not a separate project with a separate budget: it comes from the same world as the stills, in the same production. Vertical formats for social and retail. These too are concept studies, not commissioned.",
    s_studio="04 — The studio", h_studio="The person who replies is the one who makes the images",
    studio=["I am Matteo Palumbo, fashion photographer: twenty years of editorials and campaigns for international magazines and brands. MPLURE is the name I give to my work today.",
            "A campaign has always meant a location, a crew, a fitting and four to six weeks. For most brands that cost is the reason three quarters of their products never get a real campaign.",
            "I produce the same result — art-directed, on brand, in formats ready for paid, retail and e-commerce — starting from the product you already have. The technology is the production engine; what you buy is the campaign, with the eye of someone who has made campaigns for twenty years."],
    facts=[("Experience", "Twenty years of editorials and campaigns: fashion, beauty, product"),
           ("Structure", "I work alone: no hand-off between who sells and who produces"),
           ("Timing", "First delivery in 5–7 days, two revision rounds included"),
           ("Delivery", "High-resolution master files for print and out-of-home, web and social versions")],
    s_how="05 — How it works", h_how="Four steps",
    steps=[("01 Reference", "You send the product, references and any brand guidelines. A thirty-minute call."),
           ("02 Concept", "Creative concept, art direction and visual world, approved before production starts."),
           ("03 Production", "Visuals and film produced, graded and retouched in one controlled process."),
           ("04 Delivery", "First delivery in 5–7 days. Two revision rounds. Master files and web-optimised versions.")],
    s_eng="06 — Ways of working", h_eng="How I work with you",
    offers=[("Campaign still life", "Three key visuals on one product, three concepts, advertising and social formats, post-production, one revision round. The entry point for a launch or a product page."),
            ("Campaign", "Creative concept, art direction, six key visuals, two narrative settings, social formats, one short film, colour grading, two revision rounds."),
            ("Season", "Campaign identity, ten to fifteen visuals, three to five narrative scenes, three films, social and e-commerce adaptations, hero image, storyboard, master files."),
            ("Partnership", "Ongoing production: six to eight visuals and two films a month, social adaptations, campaign concepts, delivery priority.")],
    eng_note="The quote depends on formats, markets and usage rights: it arrives in writing within 24 hours of the call. Every project starts from an approved concept, no blind production.",
    s_why="07 — What I guarantee",
    why=[("Product fidelity", "Shape, logo, colour, text and finish reproduced from your reference and checked one by one against the original. Where text must be perfect, the pack is rebuilt from the original file in post-production."),
         ("Usage rights", "The delivered outputs are yours, for all channels and without time limits, unless exclusivity is agreed in the quote."),
         ("People and transparency", "No real person reproduced without a release. Where regulation requires it, the generative origin of the images is declared."),
         ("Control", "Concept approved before production, one contact from concept to master files, two revision rounds included.")],
    h_contact="Let's talk about your product.",
    p_contact="Send me a packshot and an idea of where you would like to see it. I reply personally, within one working day, with a proof proposal.",
    cta="Write to me", cta_wa="WhatsApp", avail="Open to new briefs: SS27 season",
    role="Photographer · creative direction",
    legal="The campaigns and films shown are concept studies, self-produced, not commissioned and unaffiliated with any brand. The method proofs start from public images of the products mentioned.",
)

# --------------------------------------------------------------------------- template
CSS = r"""
  :root{
    --paper:#f4f1eb; --paper-2:#ebe7df; --ink:#121110; --ink-2:#2a2825; --mute:#6f6a62;
    --rule:rgba(18,17,16,.13); --pad:clamp(22px,6vw,120px);
    --serif:"Instrument Serif",Georgia,"Times New Roman",serif;
    --sans:"Instrument Sans",-apple-system,"Segoe UI",sans-serif;
    --ease:cubic-bezier(.16,1,.3,1);
  }
  *{box-sizing:border-box;margin:0;padding:0}
  html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
  body{background:var(--paper);color:var(--ink);font-family:var(--sans);font-size:16px;line-height:1.6;-webkit-font-smoothing:antialiased}
  img{display:block;width:100%;height:auto}
  figure{margin:0} a{color:inherit;text-decoration:none}
  ::selection{background:var(--ink);color:var(--paper)}
  .grain{position:fixed;inset:0;z-index:40;pointer-events:none;opacity:.05;mix-blend-mode:multiply;
         background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .6 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}

  /* ---------- barra superiore ---------- */
  .top{position:fixed;top:0;left:0;right:0;z-index:30;display:flex;justify-content:space-between;align-items:center;
       padding:clamp(16px,2.4vw,28px) var(--pad);font-size:11px;letter-spacing:.22em;text-transform:uppercase;
       color:#fff;mix-blend-mode:difference;pointer-events:none}
  .top a,.top span{pointer-events:auto}
  .top .r{display:flex;gap:clamp(18px,3vw,40px)}
  .top a{position:relative;padding-bottom:3px}
  .top a::after{content:"";position:absolute;left:0;bottom:0;height:1px;width:100%;background:currentColor;
                transform:scaleX(0);transform-origin:right;transition:transform .6s var(--ease)}
  .top a:hover::after{transform:scaleX(1);transform-origin:left}

  /* ---------- copertina: testo a sinistra, fotografia intera a destra ---------- */
  .cover{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.05fr);min-height:100dvh;background:#0b0b0b;color:#fff}
  .cover .txt{display:flex;flex-direction:column;justify-content:flex-end;padding:clamp(120px,18vh,180px) var(--pad) clamp(34px,6vw,72px)}
  .cover figure{position:relative;overflow:hidden;min-height:60dvh}
  .cover figure img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 18%;
                    transform:scale(1.05);animation:coverImg 2.8s var(--ease) forwards}
  .eyebrow{font-size:11px;letter-spacing:.26em;text-transform:uppercase;color:rgba(255,255,255,.72);margin-bottom:24px}
  .cover h1{font-family:var(--serif);font-weight:400;font-size:clamp(58px,8vw,138px);line-height:.9;letter-spacing:-.03em}
  .cover .sub{margin-top:28px;max-width:30ch;font-family:var(--serif);font-size:clamp(20px,1.9vw,29px);line-height:1.22;color:#efece6}
  .cover .go{margin-top:36px;display:flex;align-items:center;gap:22px}
  .scroll{font-size:10px;letter-spacing:.3em;text-transform:uppercase;color:rgba(255,255,255,.6)}
  @keyframes coverImg{to{transform:scale(1)}}

  /* ---------- sezioni ---------- */
  section{padding:clamp(72px,11vw,170px) var(--pad);border-top:1px solid var(--rule)}
  .num{font-size:11px;letter-spacing:.28em;text-transform:uppercase;color:var(--mute);display:block;margin-bottom:34px}
  h2{font-family:var(--serif);font-weight:400;font-size:clamp(36px,5.2vw,74px);line-height:1;letter-spacing:-.02em;max-width:22ch;margin-bottom:34px}
  .body{max-width:58ch;font-size:clamp(16px,1.15vw,19px);color:var(--ink-2)}
  .body p + p{margin-top:18px}
  .lede{max-width:30ch;font-family:var(--serif);font-size:clamp(30px,4.2vw,60px);line-height:1.1;letter-spacing:-.015em}
  .split{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.1fr);gap:clamp(28px,5vw,90px);align-items:start}
  .split h2{margin-bottom:0}

  /* ---------- pulsanti ---------- */
  .btn{display:inline-flex;align-items:center;gap:14px;padding:12px 14px 12px 22px;border-radius:999px;border:1px solid rgba(18,17,16,.35);
       font-size:13px;letter-spacing:.08em;transition:border-color .5s var(--ease),transform .5s var(--ease),background .5s var(--ease);will-change:transform}
  .btn i{width:30px;height:30px;border-radius:999px;background:rgba(18,17,16,.07);display:inline-flex;align-items:center;justify-content:center;
         font-style:normal;transition:transform .5s var(--ease),background .5s var(--ease)}
  .btn:hover{border-color:var(--ink)} .btn:hover i{transform:translate(2px,-2px);background:rgba(18,17,16,.14)} .btn:active{transform:scale(.98)}
  .btn.light{border-color:rgba(244,241,235,.4);color:#fff} .btn.light i{background:rgba(244,241,235,.14)}
  .btn.light:hover{border-color:#fff} .btn.light:hover i{background:rgba(244,241,235,.26)}
  .btn.solid{background:var(--paper);color:var(--ink);border-color:var(--paper)} .btn.solid i{background:rgba(18,17,16,.08)}

  /* ---------- campagne ---------- */
  .work{padding-top:clamp(44px,6vw,80px);margin-top:clamp(44px,6vw,80px);border-top:1px solid var(--rule)}
  .work:first-of-type{border-top:0;margin-top:clamp(28px,4vw,52px);padding-top:0}
  .work-head{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(24px,4vw,80px);align-items:end;margin-bottom:clamp(26px,3.5vw,48px)}
  .work-meta{font-size:11px;letter-spacing:.26em;text-transform:uppercase;color:var(--mute);margin-bottom:16px}
  .work-head h3{font-family:var(--serif);font-weight:400;font-size:clamp(44px,6vw,96px);line-height:.92;letter-spacing:-.025em}
  .status{display:inline-block;border:1px solid var(--rule);border-radius:999px;padding:6px 12px;letter-spacing:.18em;font-size:10px;text-transform:uppercase;color:var(--mute);margin-top:22px}
  .work-grid{display:grid;grid-template-columns:2fr 1fr 1fr;grid-template-rows:auto auto;gap:clamp(10px,1.4vw,20px)}
  .work-grid figure{overflow:hidden;background:var(--paper-2);aspect-ratio:4/5}
  .work-grid figure:first-child{grid-row:1/3;grid-column:1}
  .work-grid figure:last-child{grid-column:2/4;aspect-ratio:8/5}
  .work-grid img{width:100%;height:100%;object-fit:cover;transition:transform 1.5s var(--ease)}
  @media (hover:hover){.work-grid figure:hover img{transform:scale(1.035)}}
  .work-film{margin-top:clamp(14px,2vw,26px);display:grid;grid-template-columns:minmax(0,34%) 1fr;gap:clamp(16px,2.4vw,34px);align-items:end}
  .work-film .cap{font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--mute);line-height:1.9;max-width:40ch;padding-bottom:10px}
  .work-film .cap b{display:block;font-family:var(--serif);font-weight:400;letter-spacing:0;text-transform:none;font-size:clamp(20px,1.7vw,26px);color:var(--ink);margin-bottom:10px;line-height:1.15}
  .mid{margin-top:clamp(48px,7vw,100px);display:flex;justify-content:flex-end}

  /* ---------- prove ---------- */
  .proofs{display:grid;grid-template-columns:1fr 1fr;gap:clamp(26px,3.6vw,56px) clamp(18px,2.4vw,36px);margin-top:clamp(40px,5vw,72px)}
  .proof.wide{grid-column:1/-1}
  .proof figure{overflow:hidden;background:var(--paper-2)}
  .proof img{transition:transform 1.5s var(--ease)}
  @media (hover:hover){.proof:hover img{transform:scale(1.02)}}
  .proof .lbl{display:flex;justify-content:space-between;font-size:10px;letter-spacing:.24em;text-transform:uppercase;color:var(--mute);margin-bottom:10px}
  .proof .cap{display:flex;justify-content:space-between;gap:24px;align-items:baseline;margin-top:14px;border-top:1px solid var(--rule);padding-top:12px}
  .proof .cap b{font-weight:500;font-size:14px;letter-spacing:.01em;white-space:nowrap}
  .proof .cap span{font-family:var(--serif);font-size:clamp(16px,1.25vw,20px);color:var(--ink-2);text-align:right;max-width:44ch}
  .note{font-size:12px;color:var(--mute);max-width:64ch;margin-top:34px;line-height:1.7}

  /* ---------- film ---------- */
  .film{position:relative;overflow:hidden;background:#0b0b0b}
  .film video{width:100%;height:auto;display:block;background:#0b0b0b}
  .films{display:grid;grid-template-columns:repeat(4,1fr);gap:clamp(12px,1.8vw,26px);margin-top:clamp(40px,5vw,72px);align-items:start}
  .films figcaption{margin-top:12px;font-size:11px;letter-spacing:.22em;text-transform:uppercase;color:var(--mute)}
  .sound{position:absolute;right:12px;bottom:12px;z-index:5;display:flex;align-items:center;gap:7px;padding:9px 13px;border:0;cursor:pointer;
         background:rgba(10,10,10,.5);color:#fff;font:inherit;font-size:9px;letter-spacing:.22em;text-transform:uppercase;border-radius:999px;
         backdrop-filter:blur(8px);opacity:0;transition:opacity .5s var(--ease),background .3s}
  .film:hover .sound,.sound:focus-visible,.sound.on{opacity:1}
  .sound .bars{display:inline-flex;align-items:flex-end;gap:2px;height:9px}
  .sound .bars i{width:2px;background:#fff;height:3px;display:block;transition:height .3s var(--ease)}
  .sound.on .bars i:nth-child(1){height:5px}.sound.on .bars i:nth-child(2){height:9px}.sound.on .bars i:nth-child(3){height:6px}
  @media (hover:none){.sound{opacity:1}}

  /* ---------- liste ---------- */
  .rows{border-top:1px solid var(--rule);max-width:110ch;margin-top:clamp(28px,4vw,52px)}
  .row{display:grid;grid-template-columns:minmax(0,24ch) 1fr;gap:clamp(16px,3vw,60px);border-bottom:1px solid var(--rule);padding:22px 0}
  .row .k{font-size:clamp(16px,1.3vw,20px);font-weight:500}
  .row .k.step{font-family:var(--serif);font-weight:400;font-size:clamp(20px,1.7vw,26px)}
  .row .v{color:var(--mute);font-size:clamp(14px,1.05vw,17px);max-width:66ch}
  .offers{display:grid;grid-template-columns:repeat(2,1fr);gap:clamp(22px,3.4vw,56px) clamp(22px,3.4vw,64px);margin-top:clamp(32px,4.5vw,64px)}
  .offer{border-top:1px solid var(--ink);padding-top:22px}
  .offer .n{font-size:11px;letter-spacing:.26em;text-transform:uppercase;color:var(--mute)}
  .offer h3{font-family:var(--serif);font-weight:400;font-size:clamp(28px,2.6vw,40px);letter-spacing:-.01em;margin:8px 0 14px;line-height:1.05}
  .offer p{font-size:15px;color:var(--ink-2);max-width:46ch}

  /* ---------- contatto ---------- */
  .contact{background:var(--ink);color:var(--paper);border-top:0;padding-bottom:clamp(40px,6vw,80px)}
  .contact .num{color:rgba(244,241,235,.55)}
  .contact h2{max-width:16ch;font-size:clamp(44px,7vw,110px)}
  .contact .body{color:rgba(244,241,235,.82)}
  .ctas{display:flex;flex-wrap:wrap;gap:14px;margin-top:38px}
  .foot{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:end;margin-top:clamp(70px,10vw,140px);padding-top:30px;
        border-top:1px solid rgba(244,241,235,.18);font-size:13px;line-height:1.9;color:rgba(244,241,235,.75)}
  .foot .wordmark{font-family:var(--serif);font-size:clamp(40px,6vw,84px);line-height:.9;letter-spacing:-.03em;color:var(--paper)}
  .foot .r{text-align:right} .foot a:hover{color:#fff;text-decoration:underline;text-underline-offset:4px}
  .foot .legal{grid-column:1/-1;font-size:11px;color:rgba(244,241,235,.45);max-width:76ch;line-height:1.7}

  /* ---------- motion ---------- */
  @media (prefers-reduced-motion:no-preference){
    .reveal{opacity:0;transform:translateY(28px);filter:blur(6px);transition:opacity 1.1s var(--ease),transform 1.1s var(--ease),filter 1.1s var(--ease)}
    .reveal.seen{opacity:1;transform:none;filter:none}
    .stagger>*{opacity:0;transform:translateY(30px);transition:opacity 1s var(--ease),transform 1s var(--ease)}
    .stagger.seen>*{opacity:1;transform:none}
    .stagger.seen>*:nth-child(2){transition-delay:.08s}.stagger.seen>*:nth-child(3){transition-delay:.16s}
    .stagger.seen>*:nth-child(4){transition-delay:.24s}.stagger.seen>*:nth-child(5){transition-delay:.32s}
    .stagger.seen>*:nth-child(6){transition-delay:.4s}.stagger.seen>*:nth-child(7){transition-delay:.48s}.stagger.seen>*:nth-child(8){transition-delay:.56s}
    .cover .eyebrow,.cover h1,.cover .sub,.cover .go{opacity:0;transform:translateY(26px);animation:up 1.3s var(--ease) forwards}
    .cover .eyebrow{animation-delay:.2s}.cover h1{animation-delay:.35s}.cover .sub{animation-delay:.6s}.cover .go{animation-delay:.85s}
    @keyframes up{to{opacity:1;transform:none}}
  }
  .progress{position:fixed;top:0;left:0;height:2px;width:0;background:#fff;z-index:35;mix-blend-mode:difference}
  .toc{position:fixed;right:clamp(14px,2vw,28px);top:50%;transform:translateY(-50%);z-index:35;display:flex;flex-direction:column;gap:10px;mix-blend-mode:difference}
  .toc a{width:20px;height:1px;background:#fff;opacity:.35;transition:opacity .5s var(--ease),width .5s var(--ease);display:block}
  .toc a.on{opacity:1;width:34px}

  @media (max-width:900px){
    .top{font-size:10px;letter-spacing:.16em;padding:14px var(--pad);white-space:nowrap}
    .top .brand span{display:none} .top .r{gap:16px} .top a.hide-m{display:none}
    .cover{grid-template-columns:1fr;grid-template-rows:auto auto;min-height:0}
    .cover figure{order:-1;height:72dvh;min-height:420px} .cover .txt{padding:36px var(--pad) 48px} .scroll{display:none}
    .split,.work-head,.offers,.foot{grid-template-columns:1fr}
    .proofs{grid-template-columns:1fr} .films{grid-template-columns:1fr 1fr}
    .work-grid{grid-template-columns:1fr 1fr;grid-template-rows:auto}
    .work-grid figure:first-child{grid-row:auto;grid-column:1/3;aspect-ratio:4/5} .work-grid figure:last-child{grid-column:auto;aspect-ratio:4/5}
    .work-film{grid-template-columns:1fr} .row{grid-template-columns:1fr;gap:6px} .foot .r{text-align:left} .toc{display:none}
    .proof .cap{flex-direction:column;gap:6px} .proof .cap span{text-align:left} .mid{justify-content:flex-start}
  }
  @media (max-width:560px){.films{grid-template-columns:1fr}}
  @media print{
    .grain,.progress,.toc,.top,.sound,.scroll,.mid{display:none}
    .reveal,.stagger>*{opacity:1!important;transform:none!important;filter:none!important}
    .cover .eyebrow,.cover h1,.cover .sub,.cover .go{opacity:1!important;animation:none!important}
    @page{margin:0;size:A4} body{font-size:10pt}
    section{padding:16mm 14mm} .cover{min-height:0;height:297mm;break-after:page;-webkit-print-color-adjust:exact;print-color-adjust:exact}
    .contact{-webkit-print-color-adjust:exact;print-color-adjust:exact}
    .work,.proof,.offer,.row,figure{break-inside:avoid;page-break-inside:avoid}
  }
"""

JS = r"""
(function(){
  var motionOK=!window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var bar=document.getElementById('progress'),ticking=false;
  function paint(){var h=document.documentElement.scrollHeight-window.innerHeight;bar.style.width=(h>0?(window.scrollY/h)*100:0)+'%';ticking=false}
  addEventListener('scroll',function(){if(!ticking){requestAnimationFrame(paint);ticking=true}},{passive:true});paint();

  var secs=[].slice.call(document.querySelectorAll('section')),toc=document.getElementById('toc');
  secs.forEach(function(s,i){if(!s.id)s.id='s'+i;var n=s.querySelector('.num'),a=document.createElement('a');a.href='#'+s.id;
    a.setAttribute('aria-label',n?n.textContent:'Cover');toc.appendChild(a)});
  var links=[].slice.call(toc.children);
  var spy=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;var i=secs.indexOf(e.target);
    links.forEach(function(l,j){l.classList.toggle('on',j===i)})})},{rootMargin:'-45% 0px -45% 0px'});
  secs.forEach(function(s){spy.observe(s)});

  var els=document.querySelectorAll('.reveal,.stagger');
  if(motionOK){var rev=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('seen');rev.unobserve(e.target)}})},
    {rootMargin:'0px 0px -10% 0px',threshold:.1});els.forEach(function(el){rev.observe(el)})}
  else{els.forEach(function(el){el.classList.add('seen')})}

  var films=[].slice.call(document.querySelectorAll('.film'));
  films.forEach(function(f){var v=f.querySelector('video');if(!v)return;
    v.muted=true;v.loop=true;v.playsInline=true;v.removeAttribute('controls');
    var btn=document.createElement('button');btn.className='sound';btn.type='button';btn.setAttribute('aria-label','Audio');
    btn.innerHTML='<span class="bars"><i></i><i></i><i></i></span><span>audio</span>';f.appendChild(btn);
    btn.addEventListener('click',function(e){e.stopPropagation();var on=v.muted;
      films.forEach(function(o){var ov=o.querySelector('video');if(ov)ov.muted=true;var ob=o.querySelector('.sound');if(ob)ob.classList.remove('on')});
      if(on){v.muted=false;if(v.paused)v.play();btn.classList.add('on')}});
    f.addEventListener('click',function(){if(v.paused)v.play();else v.pause()})});
  var vObs=new IntersectionObserver(function(es){es.forEach(function(e){var v=e.target.querySelector('video');if(!v)return;
    if(e.isIntersecting){var p=v.play();if(p&&p.catch)p.catch(function(){})}else{v.pause();v.muted=true;var b=e.target.querySelector('.sound');if(b)b.classList.remove('on')}})},{threshold:.4});
  films.forEach(function(f){vObs.observe(f)});
})();
"""

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' fill='%23121110'/%3E"
           "%3Ctext x='50%25' y='58%25' dominant-baseline='middle' text-anchor='middle' font-family='Georgia,serif' font-size='40' fill='%23f4f1eb'%3EM%3C/text%3E%3C/svg%3E")


def render(T: dict) -> str:
    p = T["prefix"]
    L = T["lang"]
    url = BASE_URL + ("en/" if L == "en" else "")
    other_url = BASE_URL + ("" if L == "en" else "en/")

    works = []
    for i, w in enumerate(WORKS):
        t = w[L]
        cells = []
        for i2, n in enumerate(w["imgs"]):
            rel = "img/%s-%s.jpg" % (w["slug"], n)
            lazy = "eager" if (i == 0 and i2 == 0) else "lazy"
            cells.append('<figure><img src="%s%s" %s alt="%s — %d" loading="%s" decoding="async"></figure>'
                         % (p, rel, dims(rel), esc(w["title"]), i2 + 1, lazy))
        grid = "\n".join(cells)
        works.append(f'''<article class="work">
  <div class="work-head reveal">
    <div><div class="work-meta">0{i+1} — {esc(t["meta"])}</div><h3>{esc(w["title"])}</h3><div class="status">{esc(T["status"])}</div></div>
    <div class="body"><p>{esc(t["body"])}</p></div>
  </div>
  <div class="work-grid stagger">{grid}</div>
  <div class="work-film reveal"><figure class="film"><video src="{p}media/{w['film']}.mp4" poster="{p}media/{w['film']}-poster.jpg" muted loop playsinline preload="metadata" aria-label="{esc(w['title'])} — film"></video></figure>
    <div class="cap"><b>{esc(T["film_lbl"])}</b>{esc(t["cap"])}</div></div>
</article>''')

    proofs = []
    for i, (slug, it, en) in enumerate(PROOFS):
        cat, desc = it if L == "it" else en
        rel = f"img/proof/{slug}.jpg"
        proofs.append(f'''<div class="proof{' wide' if i < 2 else ''}">
  <div class="lbl"><span>{esc(T["lbl_from"])}</span><span>{esc(T["lbl_to"])}</span></div>
  <figure><img src="{p}{rel}" {dims(rel)} alt="{esc(cat)} — {esc(T["lbl_from"])} / {esc(T["lbl_to"])}" loading="lazy" decoding="async"></figure>
  <div class="cap"><b>{esc(cat)}</b><span>{esc(desc)}</span></div>
</div>''')

    films = "\n".join(
        f'<figure class="film"><video src="{p}media/{f}.mp4" poster="{p}media/{f}-poster.jpg" muted loop playsinline preload="metadata" aria-label="{esc(it if L=="it" else en)}"></video><figcaption>{esc(it if L=="it" else en)}</figcaption></figure>'
        for f, it, en in FILMS)
    rows = lambda items, cls="": "\n".join(f'<div class="row"><div class="k{cls}">{esc(k)}</div><div class="v">{esc(v)}</div></div>' for k, v in items)
    offers = "\n".join(f'<div class="offer"><div class="n">0{i+1}</div><h3>{esc(k)}</h3><p>{esc(v)}</p></div>' for i, (k, v) in enumerate(T["offers"]))
    studio = "\n".join(f"<p>{esc(x)}</p>" for x in T["studio"])

    return f'''<!doctype html>
<html lang="{L}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(T["title"])}</title>
<meta name="description" content="{esc(T["description"])}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="it" href="{BASE_URL}">
<link rel="alternate" hreflang="en" href="{BASE_URL}en/">
<meta name="theme-color" content="#121110">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(T["title"])}">
<meta property="og:description" content="{esc(T["description"])}">
<meta property="og:image" content="{BASE_URL}img/og.jpg">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="{'it_IT' if L=='it' else 'en_GB'}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{FAVICON}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:wght@400;500&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<link rel="preload" as="image" href="{p}{HERO}" fetchpriority="high">
<style>{CSS}</style>
</head>
<body>
<div class="grain" aria-hidden="true"></div>
<div class="progress" id="progress"></div>
<nav class="toc" id="toc" aria-label="{esc(T["aria_sections"])}"></nav>
<header class="top"><a class="brand" href="#top">MPLURE<span> — Matteo Palumbo</span></a><div class="r"><a href="#work">{esc(T["nav_work"])}</a><a class="hide-m" href="#method">{esc(T["nav_method"])}</a><a href="#contact">{esc(T["nav_contact"])}</a><a href="{other_url}" hreflang="{'en' if L=='it' else 'it'}">{T["other_lang"]}</a></div></header>

<section class="cover" id="top">
  <div class="txt">
    <div class="eyebrow">{esc(T["eyebrow"])}</div>
    <h1>{esc(T["h1"])}</h1>
    <p class="sub">{esc(T["sub"])}</p>
    <div class="go"><a class="btn light" href="#work">{esc(T["hero_cta"])}<i>&darr;</i></a><span class="scroll">{esc(T["scroll"])}</span></div>
  </div>
  <figure><img src="{p}{HERO}" {dims(HERO)} alt="Matteo Palumbo — MPLURE, Desert Veil" fetchpriority="high" decoding="async"></figure>
</section>

<section id="positioning"><p class="lede reveal">{esc(T["lede"])}</p></section>

<section id="work">
  <span class="num">{esc(T["s_work"])}</span>
  <div class="split reveal"><h2>{esc(T["h_work"])}</h2><div class="body"><p>{esc(T["p_work"])}</p></div></div>
  {"".join(works)}
  <div class="mid reveal"><a class="btn" href="#contact">{esc(T["mid_cta"])}<i>&rarr;</i></a></div>
</section>

<section id="method">
  <span class="num">{esc(T["s_proof"])}</span>
  <div class="split reveal"><h2>{esc(T["h_proof"])}</h2><div class="body"><p>{esc(T["p_proof"])}</p></div></div>
  <div class="proofs stagger">{"".join(proofs)}</div>
  <p class="note">{esc(T["proof_note"])}</p>
</section>

<section id="motion">
  <span class="num">{esc(T["s_motion"])}</span>
  <div class="split reveal"><h2>{esc(T["h_motion"])}</h2><div class="body"><p>{esc(T["p_motion"])}</p></div></div>
  <div class="films stagger">{films}</div>
</section>

<section id="studio">
  <span class="num">{esc(T["s_studio"])}</span>
  <div class="split reveal"><h2>{esc(T["h_studio"])}</h2><div class="body">{studio}</div></div>
  <div class="rows stagger">{rows(T["facts"])}</div>
</section>

<section id="how">
  <span class="num">{esc(T["s_how"])}</span><h2 class="reveal">{esc(T["h_how"])}</h2>
  <div class="rows stagger">{rows(T["steps"], " step")}</div>
</section>

<section id="engagements">
  <span class="num">{esc(T["s_eng"])}</span><h2 class="reveal">{esc(T["h_eng"])}</h2>
  <div class="offers stagger">{offers}</div>
  <p class="note">{esc(T["eng_note"])}</p>
</section>

<section id="guarantees">
  <span class="num">{esc(T["s_why"])}</span>
  <div class="rows stagger">{rows(T["why"])}</div>
</section>

<section class="contact" id="contact">
  <span class="num">08 — {esc(T["nav_contact"])}</span>
  <h2 class="reveal">{esc(T["h_contact"])}</h2>
  <div class="body reveal"><p>{esc(T["p_contact"])}</p></div>
  <div class="ctas reveal">
    <a class="btn solid" href="mailto:matteopalumboph@gmail.com?subject=Campagna%20MPLURE">{esc(T["cta"])}<i>&rarr;</i></a>
    <a class="btn light" href="https://wa.me/393933325473" rel="noopener">{esc(T["cta_wa"])}<i>&rarr;</i></a>
    <a class="btn light" href="https://www.instagram.com/matteo_palumbo_ph" rel="noopener">Instagram<i>&rarr;</i></a>
  </div>
  <div class="foot">
    <div><div class="wordmark">MPLURE</div><div style="margin-top:14px">{esc(T["avail"])}</div></div>
    <div class="r">Matteo Palumbo<br>{esc(T["role"])}<br><a href="mailto:matteopalumboph@gmail.com">matteopalumboph@gmail.com</a><br><a href="tel:+393933325473">+39 393 332 5473</a><br><a href="https://www.instagram.com/matteo_palumbo_ph" rel="noopener">@matteo_palumbo_ph</a></div>
    <div class="legal">{esc(T["legal"])}</div>
  </div>
</section>

<script>{JS}</script>
</body>
</html>
'''


if __name__ == "__main__":
    (ROOT / "index.html").write_text(render(IT), encoding="utf-8")
    (ROOT / "en").mkdir(exist_ok=True)
    (ROOT / "en" / "index.html").write_text(render(EN), encoding="utf-8")
    print("scritti index.html e en/index.html")
