import sys, pathlib
out = pathlib.Path(sys.argv[1])
CONTACT = {"en": 'Write to <a href="mailto:snapplanetsupport@gmail.com">snapplanetsupport@gmail.com</a>. Answers in English or French.',
           "fr": 'Écrivez à <a href="mailto:snapplanetsupport@gmail.com">snapplanetsupport@gmail.com</a>. Réponses en français ou en anglais.'}
UPDATED = {"en": "21 November 2026", "fr": "21 novembre 2026"}

def page(lang, name, title, body):
    root = "" if lang == "en" else "../"
    other = ("fr/" + name) if lang == "en" else ("../" + name)
    other_label = "Français" if lang == "en" else "English"
    home = "index.html"
    nav = {"en": ("Help", "Privacy", "Terms of Use"), "fr": ("Aide", "Confidentialité", "Conditions d’utilisation")}[lang]
    html = f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="icon" href="{root}img/icon.png">
<link rel="stylesheet" href="{root}style.css">
</head>
<body>
<main>
<header><a href="{home}"><img src="{root}img/icon.png" alt=""></a><a class="home" href="{home}">SnapPlanet</a><a class="lang" href="{other}" hreflang="{'fr' if lang == 'en' else 'en'}">{other_label}</a></header>
{body}
<footer><a href="support.html">{nav[0]}</a> · <a href="privacy.html">{nav[1]}</a> · <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">{nav[2]}</a></footer>
</main>
</body>
</html>
"""
    d = out if lang == "en" else out / "fr"
    d.mkdir(parents=True, exist_ok=True)
    (d / name).write_text(html)

# ---------- Home ----------
for lang in ["en", "fr"]:
    r = "" if lang == "en" else "../"
    if lang == "en":
        body = f"""<h1>The Earth from space, any day</h1>
<p>SnapPlanet pictures any place on Earth from the free images that satellites take every few days, and processes them on your iPhone: events seen from space, before and after, timelapses since 1984, places worth a look.</p>
<div class="prints"><img src="{r}img/see.jpg" alt="Burnt areas of the Palisades fire, January 2025"><img src="{r}img/event.jpg" alt="Kakhovka dam before and after, June 2023"><img src="{r}img/earth.jpg" alt="Perito Moreno glacier, Argentina"><img src="{r}img/places.jpg" alt="Ilulissat icefjord, Greenland"></div>
<p>For iPhone and iPad. No account, no tracking.</p>
<p class="muted">Images: contains modified Copernicus Sentinel data; Landsat courtesy of the U.S. Geological Survey; MODIS courtesy of NASA; GOES from NOAA. They do not endorse SnapPlanet.</p>"""
        title = "SnapPlanet"
    else:
        body = f"""<h1>La Terre vue de l’espace, chaque jour</h1>
<p>SnapPlanet montre n’importe quel lieu de la Terre à partir des images gratuites que les satellites prennent tous les quelques jours, et les traite sur votre iPhone : les événements vus de l’espace, l’avant et l’après, des timelapses depuis 1984, des lieux à voir.</p>
<div class="prints"><img src="{r}img/see.jpg" alt="Zones brûlées de l’incendie de Palisades, janvier 2025"><img src="{r}img/event.jpg" alt="Barrage de Kakhovka avant et après, juin 2023"><img src="{r}img/earth.jpg" alt="Glacier Perito Moreno, Argentine"><img src="{r}img/places.jpg" alt="Fjord glacé d’Ilulissat, Groenland"></div>
<p>Pour iPhone et iPad. Sans compte, sans pistage.</p>
<p class="muted">Images : contient des données Copernicus Sentinel modifiées ; Landsat fournies par l’U.S. Geological Survey ; MODIS fournies par la NASA ; GOES de la NOAA. Ils ne cautionnent pas SnapPlanet.</p>"""
        title = "SnapPlanet"
    page(lang, "index.html", title, body)

# ---------- Privacy ----------
privacy = {
"en": f"""<h1>Privacy policy</h1>
<p class="muted">Last updated {UPDATED['en']}.</p>
<p><strong>In short: SnapPlanet collects nothing about you.</strong> There is no account, no analytics, no advertising and no tracking. What you make in the app stays on your devices and in your own iCloud.</p>
<h2>What stays on your device</h2>
<p>Pictures you make, searches, events and forecasts already loaded, your own views and your settings are kept on your iPhone or iPad, so the app works without a network. Deleting the app deletes them.</p>
<h2>iCloud</h2>
<p>Saved snaps and followed places are kept in your private iCloud database, so they appear on your other devices. They are stored by Apple under your Apple Account; the developer of SnapPlanet cannot see or read them.</p>
<h2>Location</h2>
<p>Only when you tap “Frame where I am”, the app reads your position once to move the map there. The position is not stored and is never sent anywhere.</p>
<h2>Photos</h2>
<p>When you save a picture, a video or a wallpaper to Photos, SnapPlanet adds it to an album named SnapPlanet. It does not read or send your other photos.</p>
<h2>Notifications and event alerts</h2>
<p>Pass reminders and change notices are scheduled on your device. If you turn on event alerts, your device saves subscriptions in Apple’s iCloud (the kinds of event you chose, and the location of followed places, to match events within 100 km), under an anonymous identifier Apple gives the app; Apple uses them to deliver the alerts. The developer cannot list them or link them to you. Turning alerts off removes them.</p>
<h2>Services the app reads</h2>
<p>To show pictures and events, the app downloads public data from: AWS Earth Search (Element 84, Sentinel-2 images), Microsoft Planetary Computer (Landsat, MODIS and GOES images), the published place and event pictures on GitHub Pages, USGS, GDACS, NASA EONET and the Copernicus Emergency Management Service, and Apple Maps. These requests carry the area being looked at, never an identifier or anything about you; like any website, these services see your device’s network address. Their own privacy policies apply to their servers.</p>
<h2>Translation</h2>
<p>Event descriptions are translated by Apple’s translation on your device.</p>
<h2>Purchases</h2>
<p>SnapPlanet Pro is bought and managed through Apple. The developer receives no payment details and no personal information.</p>
<h2>Children</h2>
<p>SnapPlanet collects no data from anyone, children included.</p>
<h2>Changes</h2>
<p>If the app ever collects data, this page will say so before that version is released, with the date above changed.</p>
<h2>Contact</h2>
<p>{CONTACT['en']}</p>""",
"fr": f"""<h1>Politique de confidentialité</h1>
<p class="muted">Dernière mise à jour le {UPDATED['fr']}.</p>
<p><strong>En bref : SnapPlanet ne collecte rien sur vous.</strong> Pas de compte, pas de statistiques, pas de publicité, aucun pistage. Ce que vous créez dans l’app reste sur vos appareils et dans votre propre iCloud.</p>
<h2>Ce qui reste sur votre appareil</h2>
<p>Les images que vous créez, les recherches, les événements et prévisions déjà chargés, vos propres vues et vos réglages sont gardés sur votre iPhone ou iPad, pour que l’app fonctionne sans réseau. Supprimer l’app les supprime.</p>
<h2>iCloud</h2>
<p>Les snaps enregistrés et les lieux suivis sont gardés dans votre base iCloud privée, pour apparaître sur vos autres appareils. Ils sont stockés par Apple sous votre compte Apple ; le développeur de SnapPlanet ne peut ni les voir ni les lire.</p>
<h2>Localisation</h2>
<p>Seulement quand vous touchez « Cadrer là où je suis », l’app lit votre position une fois pour y déplacer la carte. La position n’est pas gardée et n’est jamais envoyée.</p>
<h2>Photos</h2>
<p>Quand vous enregistrez une image, une vidéo ou un fond d’écran dans Photos, SnapPlanet l’ajoute à un album nommé SnapPlanet. L’app ne lit ni n’envoie vos autres photos.</p>
<h2>Notifications et alertes d’événements</h2>
<p>Les rappels de passage et les avis de changement sont programmés sur votre appareil. Si vous activez les alertes d’événements, votre appareil enregistre des abonnements dans l’iCloud d’Apple (les types d’événements choisis, et la position des lieux suivis, pour retenir les événements à moins de 100 km), sous un identifiant anonyme qu’Apple donne à l’app ; Apple s’en sert pour envoyer les alertes. Le développeur ne peut ni les lister ni les relier à vous. Désactiver les alertes les supprime.</p>
<h2>Services consultés par l’app</h2>
<p>Pour montrer images et événements, l’app télécharge des données publiques depuis : AWS Earth Search (Element 84, images Sentinel-2), Microsoft Planetary Computer (images Landsat, MODIS et GOES), les images de lieux et d’événements publiées sur GitHub Pages, l’USGS, le GDACS, NASA EONET et le service de gestion des urgences Copernicus, et Plans d’Apple. Ces requêtes portent la zone regardée, jamais un identifiant ni rien sur vous ; comme tout site web, ces services voient l’adresse réseau de votre appareil. Leurs propres politiques de confidentialité s’appliquent à leurs serveurs.</p>
<h2>Traduction</h2>
<p>Les descriptions d’événements sont traduites par la traduction d’Apple, sur votre appareil.</p>
<h2>Achats</h2>
<p>SnapPlanet Pro est acheté et géré par Apple. Le développeur ne reçoit aucune donnée de paiement ni information personnelle.</p>
<h2>Enfants</h2>
<p>SnapPlanet ne collecte de données sur personne, enfants compris.</p>
<h2>Modifications</h2>
<p>Si l’app venait à collecter des données, cette page le dirait avant la sortie de cette version, avec la date ci-dessus mise à jour.</p>
<h2>Contact</h2>
<p>{CONTACT['fr']}</p>"""}
for lang in ["en", "fr"]:
    page(lang, "privacy.html", "SnapPlanet · " + ("Privacy policy" if lang == "en" else "Confidentialité"), privacy[lang])

# ---------- Support ----------
faq = {
"en": [
("A picture is mostly cloud", "Satellites see the weather of the day they passed. Choose another date in the calendar: each day shows its cloud and whether it covers the whole frame. With Pro, “Remove clouds” replaces clouds with clear ground from other dates (up to half the frame)."),
("Part of the picture is grey stripes", "The satellite did not cover the whole frame that day. “Fill tiles” completes it from the nearest dates."),
("The newest pictures are missing", "Sentinel-2 images arrive within a day; Landsat about two weeks after it passed. A followed place notifies you when a new picture arrives."),
("How far back can I go?", "The last two months for free. With Pro: every year since 1984 (Landsat), 2015 (Sentinel-2) or 2001 (MODIS), and every past event."),
("Pictures are slow, or use mobile data", "A first quick preview comes at once; on Wi-Fi the sharp picture follows. On mobile data the app only sharpens when you tap “Sharpen”, and says how much it will download (a 12 km picture is about 18 MB the first time, much less afterwards)."),
("My snaps are not on my other devices", "They sync through your private iCloud: check that you are signed in to iCloud on each device, with iCloud Drive on."),
("I don’t receive event alerts", "In Following, check that alerts are on and that SnapPlanet may send notifications (iPhone Settings → Notifications). Alerts need iCloud."),
("Restore a purchase", "Settings (the gear at the top right) → Get SnapPlanet Pro → Restore purchases. Pro bought on one Apple Account works on all its devices."),
("Cancel a subscription", "In iPhone Settings → your name → Subscriptions, or in the App Store. Pro stays until the end of the period paid."),
("Delete my data", "Delete a snap from its page, or the app to remove everything on the device. Synced snaps can be removed in iPhone Settings → your name → iCloud → Manage Storage → SnapPlanet."),
],
"fr": [
("Une image est presque toute nuageuse", "Les satellites voient la météo du jour de leur passage. Choisissez une autre date dans le calendrier : chaque jour indique ses nuages et s’il couvre tout le cadre. Avec Pro, « Retirer les nuages » les remplace par le sol vu d’autres dates (jusqu’à la moitié du cadre)."),
("Une partie de l’image est rayée de gris", "Le satellite n’a pas couvert tout le cadre ce jour-là. « Compléter les tuiles » le complète avec les dates voisines."),
("Les images les plus récentes manquent", "Les images Sentinel-2 arrivent en moins d’un jour ; Landsat environ deux semaines après son passage. Un lieu suivi vous prévient quand une nouvelle image arrive."),
("Jusqu’où peut-on remonter ?", "Les deux derniers mois en gratuit. Avec Pro : chaque année depuis 1984 (Landsat), 2015 (Sentinel-2) ou 2001 (MODIS), et tous les événements passés."),
("Les images sont lentes, ou consomment des données mobiles", "Un aperçu rapide arrive d’abord ; en Wi-Fi l’image nette suit. En données mobiles, l’app n’affine que si vous touchez « Affiner », et indique ce qu’elle va télécharger (environ 18 Mo pour une image de 12 km la première fois, bien moins ensuite)."),
("Mes snaps ne sont pas sur mes autres appareils", "Ils se synchronisent par votre iCloud privé : vérifiez que vous êtes connecté à iCloud sur chaque appareil, avec iCloud Drive activé."),
("Je ne reçois pas les alertes d’événements", "Dans Suivis, vérifiez que les alertes sont activées et que SnapPlanet peut envoyer des notifications (Réglages de l’iPhone → Notifications). Les alertes ont besoin d’iCloud."),
("Restaurer un achat", "Réglages (la roue en haut à droite) → Passer à SnapPlanet Pro → Restaurer les achats. Pro acheté avec un compte Apple fonctionne sur tous ses appareils."),
("Résilier un abonnement", "Dans Réglages de l’iPhone → votre nom → Abonnements, ou dans l’App Store. Pro reste actif jusqu’à la fin de la période payée."),
("Supprimer mes données", "Supprimez un snap depuis sa page, ou l’app pour tout effacer de l’appareil. Les snaps synchronisés se suppriment dans Réglages de l’iPhone → votre nom → iCloud → Gérer le stockage → SnapPlanet."),
]}
for lang in ["en", "fr"]:
    h1 = "Help" if lang == "en" else "Aide"
    items = "\n".join(f"<h2>{q}</h2>\n<p>{a}</p>" for q, a in faq[lang])
    contact_h = "Contact" if lang == "en" else "Contact"
    body = f"<h1>{h1}</h1>\n<div class=\"card\">\n{items}\n</div>\n<h2>{contact_h}</h2>\n<p>{CONTACT[lang]}</p>"
    page(lang, "support.html", "SnapPlanet · " + h1, body)
print("ok")
