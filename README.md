# blackjack-app

A sleek and simple web-based Blackjack (21) game where you can play, bet, and get AI-powered insights to improve your strategy. Built with Flask, HTML/CSS, JavaScript, and Groq's LLaMA-3 API.

---

## 🎮 Features

- 💸 Start with 1000 coins and place bets
- 🃏 Play against the dealer with hit or stand options
- 🧠 AI strategy tips via Groq's LLaMA-3 (chatbot) based on your last 3 hands
- 🧠 Auto-calculated scores and card visuals from the Deck of Cards API
- ❤️ Beautiful, dark-themed UI with stylish fonts and buttons
- 📦 Persistent balance stored in `localStorage`

---

## 📸 Screenshots

![interface](https://github.com/user-attachments/assets/1c142438-fe39-409d-a4e0-d1bc74cd6f25)
![aiinsights](https://github.com/user-attachments/assets/10a27942-e7e0-407c-a1a2-bf8245280136)

---

## 🧭 File Structure

![image](https://github.com/user-attachments/assets/476f06e6-d425-4ffe-bec7-7959706d2ef9)

---

## 🔑 API Keys & Setup

1. Groq LLaMA-3 API Key
Sign up or log in at the Groq Console:
https://console.groq.com
Create a new API key and copy it.
In the project root, open config.py and set:
GROQ_API_KEY = "your_groq_api_key_here"

2. Deck of Cards API
No key required—this project uses the public Deck of Cards API.
Documentation and endpoints: https://deckofcardsapi.com/


