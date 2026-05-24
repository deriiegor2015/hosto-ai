from flask import Flask, request, jsonify

app = Flask(__name__)

# Читаємо налаштування з hosto.ai
def get_config():
    config = {}
    with open("hosto.ai", "r") as f:
        for line in f:
            if line.startswith("#ai key="):
                config["key"] = line.split("=")[1].strip()
            elif line.startswith("#ai model="):
                config["model"] = line.split("=")[1].strip()
            elif line.startswith("#ai owner="):
                config["owner"] = line.split("=")[1].strip()
    return config

config = get_config()

@app.route("/chat", methods=["POST"])
def chat():
    key = request.headers.get("Authorization")
    if key != config["key"]:
        return jsonify({"error": "❌ Невірний API key"}), 403

    user_input = request.json["text"]
    reply = f"Hosto ({config['model']}) відповідає {config['owner']}: {user_input}"
    return jsonify({"reply": reply})

app.run(port=5000)
