from flask import Flask, request, jsonify, render_template
import random
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    msg = data.get("message", "").lower().strip()
    noise_words = ["hi", "hello", "the", "train", "arrivals", "departure", "departures", "at", "for", "is", "please", "show", "me", "of"]
    words = msg.split()
    station_words = [word for word in words if word not in noise_words]
    if station_words:
        station_name = station_words[0].capitalize()
        train_types = ["Rajdhani", "Shatabdi", "Garib Rath", "Vande Bharat", "Express", "Mail"]
        t = random.choice(train_types)
        time = f"{random.randint(1,12)}:{random.choice(['00','15','30','45'])}"
        pf = random.randint(1,10)
        reply = f"<b>{station_name}</b> Schedule:<br>Train: {t} | Time: {time} | Platform: {pf}"
    elif "hello" in msg or "hi" in msg:
        reply = "Hello! Please enter any Indian station name (e.g., Patna, Surat, Bangalore)."
    else:
        reply = "Please enter a station name to get the schedule."
    return jsonify({"reply": reply})
if __name__ == "__main__":
    app.run(port=5000, debug=True)