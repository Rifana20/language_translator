Sure, Rifana! Let's walk through the code and then I’ll provide a clean `README.md` you can use for GitHub or documentation.

---

## ✅ Explanation of the Google Translate API Code

### 📁 File: `app.py`

```python
import streamlit as st
import requests
from dotenv import load_dotenv
import os
```

* **`streamlit`**: Used to create the web UI.
* **`requests`**: Sends HTTP requests to the Google Translate REST API.
* **`dotenv`**: Loads your API key securely from a `.env` file.
* **`os`**: Reads environment variables (like `GOOGLE_API_KEY`).

---

### 🔐 Load API Key

```python
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
```

* Loads your Google Translate API key from a `.env` file.
* Keeps your key **safe** and out of the source code.

---

### 🌍 Language Map

```python
language_map = {
    "English": "en",
    "Spanish": "es",
    "French": "fr",
    "Hindi": "hi",
    "German": "de",
    "Malayalam": "ml"
}
```

* Maps language names (for UI) to language codes (for Google Translate API).
* You can add more languages by extending this dictionary.

---

### 🖋️ Input & Language Selection

```python
text = st.text_area(...)
source = st.selectbox(...)
target = st.selectbox(...)
```

* Takes the input text.
* Lets users select source and target languages.

---

### 🚀 Translation Request

```python
params = {
    "q": text,
    "source": language_map[source],
    "target": language_map[target],
    "format": "text",
    "key": api_key
}
response = requests.post("https://translation.googleapis.com/language/translate/v2", data=params)
```

* Sends the input text and selected languages to Google Translate.
* Uses your API key to authorize the request.

---

### ✅ Display Result

```python
result = response.json()
translated = result["data"]["translations"][0]["translatedText"]
st.write(translated)
```

* Extracts and displays the translated text from the API response.

---

## 📘 README.md

Here’s a full `README.md` you can copy into your GitHub repo:

---

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

