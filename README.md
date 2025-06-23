

````markdown
# 🌍 Language Translator Bot (Google Translate API)

This is a beginner-friendly, web-based language translator built using **Streamlit** and the **Google Translate API**.  
It supports translation between multiple languages including **English**, **Hindi**, **French**, **German**, **Spanish**, and **Malayalam**.

---

## 🚀 Features

- Translate between supported languages
- Simple UI using Streamlit
- Malayalam support ✅
- Secure API key management using `.env`

---

## 🖼 Demo UI

![screenshot](screenshot.png)

---

## 🧑‍💻 Tech Stack

- [Streamlit](https://streamlit.io/)
- [Google Translate API](https://cloud.google.com/translate)
- [Python](https://www.python.org/)
- [dotenv](https://pypi.org/project/python-dotenv/)

---

## 🔧 Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/your-username/language-translator-bot.git
cd language-translator-bot
````

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
venv\Scripts\activate   # For Windows
source venv/bin/activate  # For Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Google Translate API key

Create a `.env` file:

```
GOOGLE_API_KEY=your_api_key_here
```

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

## 📦 `requirements.txt`

```txt
streamlit
requests
python-dotenv
````

---

