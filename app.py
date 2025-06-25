from flask import Flask, request, jsonify, render_template
from config import GROQ_API_KEY
import openai

app = Flask(__name__)

client = openai.OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

def decode_cards(code_string):
    value_map = {
        'A': 'ace', 'K': 'king', 'Q': 'queen', 'J': 'jack',
        '0': '10', '2': '2', '3': '3', '4': '4', '5': '5',
        '6': '6', '7': '7', '8': '8', '9': '9'
    }
    suit_map = {
        'S': 'spades', 'D': 'diamonds', 'H': 'hearts', 'C': 'clubs'
    }

    cards = code_string.split(',')
    decoded = []

    for code in cards:
        if len(code) != 2:
            continue
        val = value_map.get(code[0], code[0])
        suit = suit_map.get(code[1], code[1])
        decoded.append(f"{val} of {suit}")

    return ", ".join(decoded)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()
        history = data.get("history", [])

        if not history:
            return jsonify({"insights": "hi gambler"})

        decoded_summary = "\n".join([
            f"Hand {i+1}:\n"
            f"  Your cards: {decode_cards(h['player'])}\n"
            f"  Dealer cards: {decode_cards(h['dealer'])}\n"
            f"  Result: {h['result']}"
            for i, h in enumerate(history[-3:])
        ])

        prompt = f"""
You're a friendly blackjack coach. Give short, helpful tips based on these hands:

{decoded_summary}

Tips:
"""

        chat_completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {"role": "system", "content": "You are a casual, helpful blackjack strategy assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.7
        )

        reply = chat_completion.choices[0].message.content.strip()
        return jsonify({"insights": reply})

    except Exception as e:
        return jsonify({"insights": f"hi gambler\nerror: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)
