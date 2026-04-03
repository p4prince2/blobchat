

# BlobChat

A lightweight Python library for transforming raw chat text into structured, meaningful data.

BlobChat helps you clean, analyze, and convert chat conversations (like WhatsApp, Messenger, etc.) into useful insights — similar to how pandas works with tabular data.

---

## 🚀 Features

- 🧹 Clean and normalize chat text
    
- 🔥 Remove emojis and unwanted symbols
    
- 📊 Word count and basic text analysis
    
- 🧠 Simple, chainable API (like pandas)
    
- ⚡ Lightweight and easy to use
    

---

## 📦 Installation

```bash
pip install blobchat
```

> ⚠️ Currently under development. For latest version:

```bash
git clone https://github.com/p4prince2/blobchat.git
cd blobchat
pip install -e .
```

---

## 🧪 Quick Example

```python
from blobchat import Chat

chat = Chat("Hello BRO!!! 😄🔥 How are you?")
chat.clean().remove_symbols()

print(chat.text)
print(chat.word_count())
```

### Output:

```
hello bro how are you
5
```

---

## 🧠 Planned Features

- 📂 Read chat files (WhatsApp, etc.)
    
- 👥 Detect users and messages
    
- 📅 Extract timestamps
    
- 📊 Convert chats to DataFrame
    
- 📈 Analytics (top users, word frequency, etc.)
    
- 😊 Sentiment analysis
    

---

## 🏗️ Project Structure

```
blobchat/
├── src/blobchat/
│   ├── __init__.py
│   └── core.py
├── tests/
├── README.md
├── pyproject.toml
```

---

## 🧑‍💻 Development

Clone the repo and install in editable mode:

```bash
git clone https://github.com/p4prince2/blobchat.git
cd blobchat
pip install -e .
```

Run tests:

```bash
pytest
```

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to open issues or submit pull requests.

---

## 📄 License

MIT License

---

## 👨‍💻 Author

**Prince Kushwaha**  
GitHub: [https://github.com/p4prince2](https://github.com/p4prince2)
