# 🌍 Language Translator Bot (Google Translate API)

This is a beginner-friendly, web-based language translator built using **Streamlit** and the **Google Translate API**.  
It supports translation between multiple languages including **English**, **Hindi**, **French**, **German**, **Spanish**, and **Malayalam**.

---

## 🚀 Features

- 🌐 Translate between multiple supported languages
- 🧠 Smart interface using Streamlit
- ✅ Malayalam included!
- 🔐 Secure API key management using `.env`

---

## 🖼 Demo UI

![screenshot](screenshot.png)

---

## 🧑‍💻 Tech Stack

- [Streamlit](https://streamlit.io/)
- [Google Translate API](https://cloud.google.com/translate)
- [Python](https://www.python.org/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)

---

## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/language-translator-bot.git
cd language-translator-bot
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
venv\Scripts\activate        # On Windows
# OR
source venv/bin/activate     # On macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Google Translate API key

Create a `.env` file in the root directory with:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

You can generate an API key from: https://console.cloud.google.com/apis/credentials

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open: http://localhost:8501 in your browser.

---

## 🧪 Run the App

```bash
streamlit run app.py
```

Then go to [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🌐 Language Support

| Language  | Code |
| --------- | ---- |
| English   | en   |
| Hindi     | hi   |
| Malayalam | ml   |
| French    | fr   |
| German    | de   |
| Spanish   | es   |

---

## ✅ Sample Test Cases

| Text              | From      | To      | Expected Output    |
| ----------------- | --------- | ------- | ------------------ |
| My name is Rifana | English   | Hindi   | मेरा नाम रिफाना है |
| Bonjour           | French    | English | Hello              |
| നമസ്കാരം          | Malayalam | English | Hello              |

---

## 📜 License

MIT License — feel free to use and modify for learning purposes.

---

## 💡 Credits

Made with ❤️ using Google Translate API and Streamlit.

````

---



