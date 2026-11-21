# SnapPlanet site

The SnapPlanet app's public pages, in English and French: home, help (`support.html`) and privacy policy
(`privacy.html`), served by GitHub Pages at https://jjrom.github.io/snapplanet-site/. The app links to them
from its Pro sheet and Settings (`SiteLinks` in the app's `ProView.swift`). Plain HTML and one stylesheet;
the colours are the app's (`DESIGN.md`). A domain can be pointed here later without changing the pages.

The pages are made by `make_site.py` (texts in English and French, contact address, last-updated date): edit it,
then run `python3 make_site.py .` and commit. The privacy policy must change before any app version that
collects data.
