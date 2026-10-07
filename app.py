import hmac, json, os
from pathlib import Path
from flask import Flask, jsonify, request, send_from_directory

BASE = Path(__file__).parent
DATA = BASE / "data"
app = Flask(__name__, static_folder="static", static_url_path="/static")


def load(name):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def save(name, obj):
    (DATA / name).write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


@app.get("/")
def home():
    return send_from_directory("static", "index.html")


@app.get("/admin")
def admin():
    return send_from_directory("static", "admin.html")


@app.get("/api/data")
def api_data():
    return jsonify(products=load("products.json"), areas=load("areas.json"))


@app.put("/api/products")
def api_update():
    key = os.environ.get("ADMIN_KEY", "")
    given = request.headers.get("X-Admin-Key", "")
    if not key or not hmac.compare_digest(key, given):
        return jsonify(error="Galat admin key"), 403
    items = request.get_json(silent=True)
    if not isinstance(items, list):
        return jsonify(error="Invalid data"), 400
    save("products.json", items)
    return jsonify(ok=True, count=len(items))


@app.get("/health")
def health():
    return "ok"


if __name__ == "__main__":
    app.run(debug=True, port=5000)
