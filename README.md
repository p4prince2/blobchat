# BlobChat

A lightweight Python library for transforming messy chat text into clean, meaningful data.
 
BlobChat helps you clean, normalize, and process chat conversations (WhatsApp, Messenger, etc.) — similar to how pandas works with structured data.

---

## 🚀 Features

* 🧹 Clean and normalize chat text
* 🔤 Convert slang to meaningful text (`u → you`, `gr8 → great`)
* 😂 Remove emojis and unwanted symbols
* ⚡ Fast and lightweight
* 🧠 Simple API for preprocessing chat data
* 🛠 CLI support for quick usage

---   

## 📦 Installation

```bash
pip install blobchat
```

> ⚠️ For latest development version:

```bash
git clone https://github.com/p4prince2/blobchat.git
cd blobchat
pip install -e .
```

---

## 🧪 Quick Example

```python
from blobchat.cleaner import clean_text

text = "u r gr8 lol 😂"
cleaned = clean_text(text)

print(cleaned)
```

### Output:

```
you are great laughing
```

---

## ⚡ Alternative API

```python
from blobchat.main import process_chat

text = "brb ttyl!"
print(process_chat(text))
```

---

## 💻 CLI Usage

```bash
blobchat "u r awesome bro ilu 😂"
```

---

## 🧠 Slang Dictionary

Slang mappings are stored in:

```
src/blobchat/slang_dict.py
```

You can extend it easily:

```python
SLANG_DICT = {
    "u": "you",
    "r": "are",
    "idk": "i don't know",
}
```

---

## 🏗️ Project Structure

```
blobchat/
├── src/blobchat/
│   ├── __init__.py
│   ├── main.py
│   ├── cleaner.py
│   ├── slang_dict.py
│   ├── utils.py
│   ├── cli.py
│   └── py.typed
│
├── tests/
│   └── test_blobchat.py
│
├── dist/
├── pyproject.toml
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🧪 Running Tests

```bash
pytest
```

---

## 📦 Build & Publish

```bash
python -m build
twine upload dist/*
```

---

## 🧠 Planned Features

* 📂 Read chat files (WhatsApp, Telegram, etc.)
* 👥 Detect users and messages
* 📅 Extract timestamps
* 📊 Convert chats to structured format (DataFrame-like)
* 📈 Analytics (word frequency, top users)
* 😊 Sentiment analysis

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Make changes
4. Submit a PR

---

## 📄 License

MIT License

---

## 👨‍💻 Author

**Prince Kushwaha**
GitHub: https://github.com/p4prince2

---

⭐ If you like this project, consider giving it a star!
