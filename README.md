# Ekdanta Distributors – Website (Flask + HTML/CSS/JS)

## Structure
```
ekdanta-distributor/
├── app.py              # Backend (Flask API)
├── data/
│   ├── products.json   # Products / stock / rates
│   └── areas.json      # Nashik areas + retailer count
├── static/             # Frontend
│   ├── index.html
│   ├── style.css
│   ├── app.js
│   └── admin.html      # Stock update page (/admin)
├── requirements.txt
├── render.yaml
└── .gitignore
```

## VS Code me chalana
1. Folder VS Code me kholein (File > Open Folder).
2. Terminal (Ctrl + `) me:
```
python -m venv .venv
.venv\Scripts\activate        # Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
set ADMIN_KEY=mykey123        # Mac/Linux: export ADMIN_KEY=mykey123
python app.py
```
3. Browser: http://127.0.0.1:5000  |  Admin: http://127.0.0.1:5000/admin

## Render par deploy
1. Folder ko GitHub repo me push karein (git init, git add ., git commit, git push).
2. render.com > New > Blueprint (ya Web Service) > repo chunein.
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn app:app`
3. Environment me `ADMIN_KEY` set karein (Blueprint me auto ban jaata hai).
4. Deploy ke baad `https://<naam>.onrender.com` live hoga.

## Zaroori notes
- WhatsApp number `static/app.js` (NUM) aur `static/index.html` ke links me hai: 918104897876.
- Facebook/Instagram links `static/index.html` footer me `href="#"` ki jagah daalein.
- Render free plan par file system temporary hai: /admin se kiya badlav redeploy/restart par
  `data/products.json` se reset ho sakta hai. Pakka rakhne ke liye products.json ko GitHub par update karein
  ya Render Disk / database use karein.
- Free plan 15 min inactivity ke baad sleep hota hai, pehla load slow ho sakta hai.
